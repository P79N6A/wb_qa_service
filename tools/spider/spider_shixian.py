#encoding:utf-8

import os
import urllib2
from sgmllib import SGMLParser

import sys


def get_shixian(url):
    # url = 'http://shixian.com/job/beijing?territory=backend'
    response = urllib2.urlopen(url)
    if 200 != response.code:
        print '请求响应状态码 %s' % (response.code)
        return
    result = response.read()

    print '-------------------------------'
    listjobs = ListJobs()
    listjobs.feed(result)
    for item in listjobs.jobs:
        item = str(item).strip()
        if item:
            print item

    print '-------------------------------'
    new_lines = []
    listhref = ListHref()
    listhref.feed(result)
    if not os.path.exists('shixian_hrefs'):
        with open('shixian_hrefs', 'w') as foo:
            foo.write('实现网兼职信息  http://shixian.com\n')
    with open('shixian_hrefs', 'r') as foo:
        lines = foo.readlines()

    for item in listhref.hrefs:
        item = str(item).strip()
        if item and item+'\n' not in lines:
            lines.append(item)
            new_lines.append(item)
            with open('shixian_hrefs', 'a') as foo:
                foo.write(item + '\n')
            print '新增加: http://shixian.com/' + item.strip('/')
    return new_lines


class ListJobs(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_job = ""
        self.jobs = []

    def start_div(self, attrs):
        for k, v in attrs:
            if k == 'class' and v == 'job':
                self.is_job = 1

    def end_div(self):
        self.is_job = ""

    def handle_data(self, text):
        if self.is_job == 1:
            self.jobs.append(text)


class ListHref(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_job = ""
        self.hrefs = []

    def start_a(self, attrs):
        if len(attrs) == 2:
            i = 0
            for k, v in attrs:
                if k == 'target' and v == '_blank':
                    i += 1
                if k == 'href' and '/jobs/' in v:
                    i += 1
            if i == 2:
                self.is_job = 1
                for k, v in attrs:
                    if k == 'href':
                       self.hrefs.append(v)

    def end_a(self):
        self.is_job = ""

if __name__ == '__main__':
    news = []
    # url_beijing_backend = 'http://shixian.com/job/beijing?territory=backend'
    # news_backend = get_shixian(url_beijing_backend)
    url_jobs = 'http://shixian.com/jobs'
    news_jobs = get_shixian(url_jobs)
    news.extend(news_jobs)

    print '总共增加jobs:    %s' % (len(news))
    if news:
        sys.exit(0)
    else:
        sys.exit(1)