#encoding:utf-8

import urllib2
from bs4 import BeautifulSoup

def get():
    titles = []
    ios_url = 'http://ota.client.weibo.cn/ios/gpackages/com.sina.weibo?pkg_type=0&page=0'
    response = urllib2.urlopen(ios_url)
    if 200 != response.code:
        print '请求响应状态码 %s' % (response.code)
        return
    result = response.read()
    soup = BeautifulSoup(result)

    #获取列表名
    for child in soup.body.children:
        if 'table' == child.name and None != child.get('border'):
            for grand in child:
                if 'tr' == grand.name and None == grand.get('onmouseout'):
                    for gg in grand:
                        if 'td' == gg.name:
                            titles.append(gg.string)

    for child in soup.body.children:
        if 'table' == child.name and None != child.get('border'):
            for grand in child:
                if 'tr' == grand.name and None != grand.get('onmouseout'):
                    for gg in grand:
                        if 'td' == gg.name:
                            # titles.append(gg.string)
                            print gg.string




if __name__ == '__main__':
    get()