from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'filestore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^file/', include('file.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('loginsys.urls')),
)
