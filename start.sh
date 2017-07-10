#!/usr/bin/env bash
DIR=$(pwd)
profile=$1
export DJANGO_SETTINGS_MODULE="qa_service.settings_${profile}"

if [ -f run.pid ]; then
    echo "server is already running"
else
    gunicorn --config qa_service/gunicorn.conf.py qa_service.wsgi:application
fi