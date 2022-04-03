from django.conf import settings
from django_hosts import patterns, host
from django.urls import path,include
from django.contrib import admin



urlpatterns=[
     path('',admin.site.urls,name="admin")
 ]


host_patterns = patterns('',
    host('',settings.ROOT_URLCONF,name='www'),
    host('admin','iste.hosts',name="admin"),
)

