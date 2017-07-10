#encoding:utf-8

from api.views import Retrun2SCM, PreviewTrigger, Health

__author__ = 'muli1'

from django.conf.urls import patterns, url

urlpatterns = patterns('api.views',

        # url(r'health', Health.as_view()),

        url(r'previewTrigger', PreviewTrigger.as_view()),   #自动化预览分发接口

        url(r'return2scm', Retrun2SCM.as_view()),           #自动化预览回调接口

    )