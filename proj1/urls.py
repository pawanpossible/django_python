from django.contrib import admin
from django.conf.urls import patterns, include, url
from login.views import *


urlpatterns = [
    #url(r'^$', index, name='index'),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^adduser/$', add_user),
    url(r'^admin/', admin.site.urls),
    url(r'^adddepartment/', add_department),
    url(r'^deleteuser/$', delete_user),
    url(r'^deletedepartment/$', delete_department),
]


