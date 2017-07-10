#encoding:utf-8
import json
import random

import time

import requests

last_time = int(time.time()) - 60 * 60 * 3
last_mid = (last_time - 515483463) << 22

def generate(f, count):
    cc = 0
    with open('uid.white', 'r') as file:
        while True:
            line = file.readline()
            if line:
                temp = line.split()
                if len(temp) == 3:
                    uid = temp[0]
                    url = 'http://i2.api.weibo.com/2/statuses/user_timeline/ids.json?source=646811797&feature=1' \
                          '&uid=%s&since_id=%s' % (str(uid), str(last_mid))
                    response = requests.get(url)
                    time.sleep(0.005)
                    if response.status_code != 200:
                        continue
                    json_response = json.loads(response.content)
                    if json_response['statuses']:
                        print '开始打印一个uid:%s 的所有结果---------------' % str(uid)
                        for mid in json_response['statuses']:
                            debug_id = random.randint(1000000000, 9999999999)
                            url_prefix = '/2/recommendation/general_recommend_body.json?domain=5&test_environment=true&source=646811797&uid=1966695840&type=6&count=15&detail=true&filter_read=true&debug_id=%s&id=' % debug_id
                            url_body = url_prefix + mid
                            print url_body
                            f.write(url_body + '\n')
                            cc += 1
                            if cc >= count:
                                return
                            print cc

if __name__ == '__main__':
    count = 100000
    with open('recommend_body', 'w') as f:
        generate(f, count)
