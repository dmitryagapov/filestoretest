from django.shortcuts import render_to_response

# Create your views here.

# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, FileResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from filestore.settings import MEDIA_ROOT
from django.contrib.auth.models import User
from loginsys.models import MyUser, UserFiles
from file.models import File
from file.forms import FileForm
from django.conf import settings
from django.core.context_processors import csrf
import logging

import os
import hashlib

logger = logging.getLogger(__name__)


def hash_file(filename):
    h = hashlib.sha1()

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()


def duplicate_file_message(hash_file):
    duplicate_files = UserFiles.objects.filter(file_hash=hash_file)
    file_user_list = ['This file already uploaded:']
    user_message_template = 'User: %s'
    file_message_template = 'File name: %s'
    for file in duplicate_files:
        file_user_list.append(user_message_template % file.file_user.user.username)
        file_user_list.append(file_message_template % file.file_name)
    return file_user_list


def user_files(request):
    try:
        user_user = User.objects.get(username=request.session['user'])
        user_my = MyUser.objects.get(user=user_user)
        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)

            if form.is_valid():
                newfile = File(content=request.FILES['content'])
                newfile.save()
                file_hash = hash_file(newfile.content.path)
                user_my.file_number += 1
                user_my.save()
                user_file_name = newfile.content.name[6:]
                try:
                    check_user_file = UserFiles.objects.get(file_user=user_my)

                    if file_hash == check_user_file.file_hash:
                        request.session['uploaded_file_status'] = ['This file already uploaded with name: %s' % check_user_file.file_name]
                        return HttpResponseRedirect(reverse('file.views.user_files'))
                    elif user_file_name == check_user_file.file_name:
                        request.session['uploaded_file_status'] = ['You already have file with such name: %s' % user_file_name]
                        return HttpResponseRedirect(reverse('file.views.user_files'))
                except UserFiles.DoesNotExist:
                    pass

                if os.path.isfile(MEDIA_ROOT + '/' + file_hash):
                    request.session['uploaded_file_status'] = duplicate_file_message(file_hash)
                    file = File.objects.get(content=file_hash)
                    file.file_links += 1
                    file.save()
                else:
                    request.session['uploaded_file_status'] = ['File is loaded successfully']
                    os.rename(newfile.content.path, MEDIA_ROOT + '/' + file_hash)
                    newfile.content.name = file_hash
                    newfile.file_links += 1
                newfile.save()
                userfile = UserFiles(file_hash=file_hash, file_name=user_file_name, file_user=user_my)
                userfile.save()

                return HttpResponseRedirect(reverse('file.views.user_files'))
        else:
            form = FileForm()

        files = UserFiles.objects.filter(file_user=user_my)

        return render_to_response(
            'files.html',
            {
                'files': files,
                'form': form,
                'username': auth.get_user(request).username,
                'uploaded_file_status': request.session['uploaded_file_status'],
            },
            context_instance=RequestContext(request)
        )
    except KeyError:
        redirect('/auth/login/')


def delete_file(request, file_hash):
    user_user = User.objects.get(username=request.session['user'])
    user_my = MyUser.objects.get(user=user_user)
    if request.session['user'] == auth.get_user(request).username:
        user_file_for_deleting = UserFiles.objects.filter(file_user=user_my).get(file_hash=file_hash)
        global_file = File.objects.get(content=file_hash)
        global_file.file_links -= 1
        global_file.save()
        user_file_for_deleting.delete()
        if global_file.file_links == 0:
            os.remove(settings.MEDIA_ROOT + '/' + file_hash)
            global_file.delete()

    return redirect('/file/user/')

def download_file(request, file_hash, file_name):
    file_size = os.path.getsize(settings.MEDIA_ROOT + '/' + file_hash)
    response = FileResponse(open(settings.MEDIA_ROOT + '/' + file_hash))
    response['Content-Disposition'] = 'attachment; filename=\"' + file_name + '\"'
    response['Content-Length'] = str(file_size)
    response['Content-Type'] = 'taplication/x-gzip'

    return response

    # return redirect('/file/user/')



