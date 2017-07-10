#encoding:utf-8

from settings import *

# 自动化线上预览分发和回调接口使用
JENKINS_HOME='http://10.210.130.44:8070/jenkins'
CALLBACK_SCM='http://10.75.1.110/scm_plat_data/services/scmPlatPiplineService/platformTestNodeCallback'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'muli',  # Or path to database file if using sqlite3.
        'USER': 'searchqa',  # Not used with sqlite3.
        'PASSWORD': 'searchqa',  # Not used with sqlite3.
        'HOST': '10.210.230.54',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    }, 'sjws_pay': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'muli',  # Or path to database file if using sqlite3.
        'USER': 'searchqa',  # Not used with sqlite3.
        'PASSWORD': 'searchqa',  # Not used with sqlite3.
        'HOST': '10.210.230.54',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    },
}