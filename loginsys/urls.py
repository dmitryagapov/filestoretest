from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project_new.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^register/', 'loginsys.views.register'),
    url(r'^$', 'loginsys.views.login'),
)
