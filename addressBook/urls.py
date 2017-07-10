#encoding:utf-8

from api.views import Retrun2SCM, PreviewTrigger, Health

__author__ = 'muli1'

from django.conf.urls import patterns, url

urlpatterns = patterns('addressBook.views',


        url(r'add', 'add'),
        url(r'regist', 'regist'),
        url(r'login', 'my_login'),
        url(r'logout', 'my_logout'),
        url(r'welcome', 'welcome'),
    )