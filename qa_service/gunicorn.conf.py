#encoding:utf-8
__author__ = 'muli1'
import multiprocessing
import os
from datetime import datetime
#example:https://github.com/disqus/channels/blob/master/gunicorn.conf.py
working_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
bind = "0.0.0.0:8071"
workers = multiprocessing.cpu_count() * 2 + 1
# worker_class = 'egg:gunicorn#gevent'
daemon = True
pidfile = '%s/run.pid' % working_dir
proc_name = 'gunicorn_qa_service'
logconfig = "%s/qa_service/gunicorn.log.conf" % working_dir
access_log_format = '%(h)s\t%(l)s\t%(u)s\t%(t)s\t"%(r)s"\t%(s)s\t%(b)s\t"%(f)s"\t"%(a)s"\t"%({X-Real-IP}i)s"'
