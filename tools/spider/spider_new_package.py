#encoding:utf-8

import os
import urllib2
from sgmllib import SGMLParser

import time

import sys


def get_packages(url, timeStamp_file):
    #爬取页面数据
    # url = 'http://shixian.com/job/beijing?territory=backend'
    response = urllib2.urlopen(url)
    if 200 != response.code:
        print '请求响应状态码 %s' % (response.code)
        return
    result = response.read()
    listpackages = ListPackages()
    listpackages.feed(result)

    #将爬去的数据分条解析
    if len(listpackages.packages) % 3 != 0:
        print '获取数据或解析数据有误'
        return
    list_json_packages = []
    for i in range(0, len(listpackages.packages), 3):
        temp = {}
        temp['version'] = listpackages.packages[i]
        temp['time'] = stringTimeToInt(listpackages.packages[i + 1])
        temp['desc'] = listpackages.packages[i + 2]
        list_json_packages.append(temp)
    list_json_packages.sort(key=lambda x: x['time'], reverse=True)

    #爬取的数据中最早时间大于记录最后时间戳时间,则返回中 continue为True, 返回时间大于记录中时间戳的数据
    lastTimeStamp = int(time.time())
    if not os.path.exists(timeStamp_file):
        with open(timeStamp_file, 'w') as foo:
            foo.write('lastTimeStamp:%s' % lastTimeStamp)

    with open(timeStamp_file, 'r') as foo:
        line = foo.readline()
        if line.strip():
            lastTimeStamp = int(line.split(':')[1])

    conitune = False
    if int(list_json_packages[-1]['time']) >= lastTimeStamp:
        conitune = True
    new_packages = []
    for item in list_json_packages:
        if int(item['time']) > lastTimeStamp:
            new_packages.append(item)

    return conitune, new_packages


class ListPackages(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_package = ""
        self.packages = []
        self.count = 0

    def start_tr(self, attrs):
        if len(attrs) == 2:
            i = 0
            for k, v in attrs:
                if k == 'onmouseout' and v == "this.style.backgroundColor='#ffffff'":
                    i += 1
                if k == 'onmouseover' and v == "this.style.background='#c1c1c1'":
                    i += 1
            if i == 2:
                self.is_package = 1

    def end_tr(self):
        self.is_package = ""

    def handle_data(self, text):
        if self.is_package == 1:
            text = str(text).strip()
            if text and text != 'Y' and text != '下载' and text != '安装':
                self.packages.append(text)



def get_all_packages(url_prefix, v):
    try:
        conitune = True
        page_num = 0
        all_news = []   #脚本执行会获取所有新加的包信息
        while conitune:
            timeStamp_file = 'lastTimeStamp_' + v
            url = url_prefix + str(page_num)
            conitune, news = get_packages(url, timeStamp_file)
            all_news.extend(news)
            page_num += 1

        if all_news:
            all_news.sort(key=lambda x: x['time'], reverse=True)
            newTimeStamp = all_news[0]['time']

            # 更新最后时间戳
            with open(timeStamp_file, 'w') as foo:
                foo.write('lastTimeStamp:%s' % newTimeStamp)
            print '------------------------------------ %s 新添加的所有包 ------------------------------------' % (v)
            for item in all_news:
                print '包版本:%s  发布时间:%s    描述:%s' % (item['version'], intTimeToString(item['time']), item['desc'])

            alpha2 = []
            for item in all_news:
                if 'alpha2' in item['version'] or 'alpha_2' in item['version']:
                    alpha2.append(item)
            if alpha2:
                print '------------------------------------ %s 新添加的alpha2包 ------------------------------------' % (v)
                for item in alpha2:
                    print '包版本:%s  发布时间:%s    描述:%s' % (item['version'], intTimeToString(item['time']), item['desc'])
                return True
            else:
                print '------------------------------------  %s 没有新添alpha2包  ------------------------------------' % (v)

        else:
            print '------------------------------------  %s 没有新添加包  ------------------------------------' % (v)
        return False

    except Exception, e:
        print e.message

def intTimeToString(timeStamp):
    timeArray = time.localtime(timeStamp)
    stringStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return stringStyleTime

def stringTimeToInt(stringStyleTime):
    timeArray = time.strptime(stringStyleTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

if __name__ == '__main__':
    ios_prefix = 'http://ota.client.weibo.cn/ios/gpackages/com.sina.weibo?pkg_type=0&page='
    android_prefix = 'http://ota.client.weibo.cn/android/gpackages/com.sina.weibo?pkg_type=0&page='
    assert_ios = get_all_packages(ios_prefix, 'ios')
    assert_android = get_all_packages(android_prefix, 'android')
    if assert_ios or assert_android:
        sys.exit(0)
    else:
        sys.exit(1)