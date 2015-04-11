# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from loginsys.models import MyUser

from django.core.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session.set_expiry(600)
            request.session['user'] = username
            request.session['uploaded_file_status'] = ['Upload the file!']
            return redirect('/file/user/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/auth/login/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid() and len(newuser_form.cleaned_data['username']) > 5 and len(newuser_form.cleaned_data['password2']) > 5:
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            request.session.set_expiry(600)
            user_my = MyUser(user=User.objects.get(username=newuser_form.cleaned_data['username']))
            user_my.save()
            request.session['user'] = newuser_form.cleaned_data['username']
            request.session['uploaded_file_status'] = ['Upload the file!']
            return redirect('/file/user/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)
