#encoding:utf-8
import json
import random
import unittest

import requests
import time


last_time = int(time.time()) - 60 * 60
last_mid = (last_time - 515483463) << 22


all_code = [201, 202, 204, 203, 205, 206]

class GeneralRecommendBody(unittest.TestCase):

    def testAll(self):
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
                        if response.status_code != 200:
                            continue
                        json_response = json.loads(response.content)
                        if json_response['statuses']:
                            print '开始打印一个uid:%s 的所有结果---------------' % str(uid)
                            for mid in json_response['statuses']:
                                time.sleep(0.1)
                                debug_id = random.randint(1000000000, 9999999999)
                                url_prefix = 'http://172.16.105.69:8080/2/recommendation/general_recommend_body.json?domain=5&test_environment=true&source=646811797&uid=1966695840&type=6&count=15&detail=true&filter_read=true&debug_id=%s&id=' % debug_id
                                url_body = url_prefix + mid
                                response = requests.get(url_body)
                                json_response = json.loads(response.content)
                                results = json_response['results']
                                if len(results) != 15:
                                    print '响应结果数不等于15, 而是%s' % len(results)
                                print '开始打印mid:%s 的一次结果' % str(mid)
                                for result in results:
                                    print result['recommend_source']
                                    if result['recommend_source'] == 201:
                                        print '遇到 201 了'
                                    # if result['recommend_source'] == 202:
                                    #     print '遇到 202 了'
                                    # if result['recommend_source'] == 204:
                                    #     print '遇到 204 了'
                                    if result['recommend_source'] == 203:
                                        print '遇到 203 了'
                                    # if result['recommend_source'] == 205:
                                    #     print '遇到 205 了'
                                    # if result['recommend_source'] == 206:
                                    #     print '遇到 206 了'
                                print '---------------'
                            print '-----------------------------------------------------'


    def testSingle(self):
        for i in range(0, 200):
            time.sleep(1)
            mid = '4034853378619869'
            debug_id = random.randint(1000000000, 9999999999)
            debug_id = '123'
            url_prefix = 'http://172.16.105.69:8080/2/recommendation/general_recommend_body.json?domain=5&test_environment=true&source=646811797&uid=1966695840&type=6&count=15&detail=true&filter_read=true&debug_id=%s&id=' % debug_id
            url_body = url_prefix + mid
            response = requests.get(url_body)
            json_response = json.loads(response.content)
            results = json_response['results']
            if len(results) != 15:
                print '响应结果数不等于15, 而是%s' % len(results)
            print '开始打印mid:%s 的一次结果' % str(mid)
            sources = []
            for result in results:
                resource = result['recommend_source']
                sources.append(resource)
                # print resource
                if resource not in all_code:
                    print '%s not in all_code' % resource
            print sources
            if 202 not in sources:
                print '202 没了'

            print '---------------'
