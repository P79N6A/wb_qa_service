#encoding:utf-8

import json
import unittest

import requests
import time


class forginCityHot(unittest.TestCase):

    def testForginCity(self):
        mids = []
        uid = '1966695840'
        debug_id = '23'
        province_id = '8008632010000000000'

        url = 'http://172.16.105.69:8080/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=%s&type=6&count=20&detail=true&filter_read=true&debug_id=%s&domain=5&province_id=%s&category=surrounding:hot' % (uid, debug_id, province_id)
        while True:
            result = requests.get(url)
            if result.status_code == 200:
                content = json.loads(result.content)
                print content
                for result in content['results']:
                    if result['id'] not in mids:
                        mids.append(result['id'])
                    else:
                        print 'have same mid'
                    print result['recommend_source']
            time.sleep(1)


    def testDomesticCityHot(self):
        mids = []
        uid = '1966695840'
        debug_id = '3241243'
        province_id = '8008651010000000000'

        url = 'http://172.16.105.69:8080/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=%s&type=6&count=20&detail=true&filter_read=true&debug_id=%s&domain=5&province_id=%s&category=surrounding:hot' % (
        uid, debug_id, province_id)
        while True:
            whitelist = toutiao = xiancheng = lvyou = remen = lbs = 0
            result = requests.get(url)
            if result.status_code == 200:
                content = json.loads(result.content)
                print content
                for result in content['results']:
                    if result['id'] not in mids:
                        mids.append(result['id'])
                    else:
                        print 'have same mid'

                    source = result['recommend_source']
                    print source
                    if None == source:
                        continue
                    if source == 101:
                        whitelist += 1
                    elif source == 102:
                        remen += 1
                    elif source == 103:
                        xiancheng += 1
                    elif source == 104:
                        toutiao += 1
                    elif source == 105:
                        lbs += 1
                    elif source == 106:
                        lvyou += 1
                print '白名单:%s, 头条:%s, 鲜城:%s, 旅游长文:%s, 热门话题本地榜:%s, LBS数据:%s' % (whitelist, toutiao, xiancheng, lvyou, remen, lbs)
                # self.assertEqual(101, content['results'][0]['recommend_source'])
                # self.assertEqual(101, content['results'][1]['recommend_source'])
                # self.assertEqual(101, content['results'][2]['recommend_source'])
                # self.assertEquals(5, toutiao)
                # self.assertEqual(1, xiancheng)
                # self.assertEqual(1, lvyou)
                # self.assertEqual(1, remen)
                # self.assertEqual(1, lbs)
            #TODO name字段都是空的,判断用省会城市物料补充
            time.sleep(1)


    def testVideo(self):
        mids = []
        uid = '1966695840'
        debug_id = '2340101'
        province_id = '8000136061000000001'

        url = 'http://172.16.105.69:8080/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=%s&type=6&count=20&detail=true&filter_read=true&debug_id=%s&domain=5&province_id=%s&category=surrounding:video' % (
            uid, debug_id, province_id)
        previous_score = -999
        previous_hotweibo_score = -999
        whitelist = lbs = huifang = hotweibo = 0
        while True:
            result = requests.get(url)
            if result.status_code == 200:
                content = json.loads(result.content)
                print content
                for result in content['results']:
                    if result['id'] not in mids:
                        mids.append(result['id'])
                    else:
                        print 'have same mid'
                        self.assertFalse()

                    source = result['recommend_source']
                    if source not in (141, 142, 143, 144):
                        self.assertFalse("wrong source")

                    this_score = result['ctr']
                    print "source:%s    score:%s" % (source, this_score)
                    if source in (141, 142, 143):
                        if previous_score != -999:
                            self.assertTrue(previous_score >= this_score)
                        previous_score = this_score
                    if source == 144:
                        if previous_hotweibo_score != -999:
                            self.assertTrue(previous_hotweibo_score >= this_score)
                        previous_hotweibo_score = this_score

                    if source == 141:
                        whitelist += 1
                    elif source == 142:
                        lbs += 1
                    elif source == 143:
                        huifang += 1
                    elif source == 144:
                        hotweibo += 1
            print '白名单:%s, LBS:%s, 直播回放:%s, 热门微博:%s' % (whitelist, lbs, huifang, hotweibo)


            time.sleep(0.5)


    def testDeliciousFood(self):
        mids = []
        uid = '1966695840'
        debug_id = '343334'
        province_id = '8008611000000000000'
        previous_score = -999
        previous_hotweibo_score = -999
        url = 'http://172.16.105.69:8080/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=%s&type=6&count=20&detail=true&filter_read=true&debug_id=%s&province_id=%s&domain=5&category=surrounding:delicacy' % (
            uid, debug_id, province_id)
        xiancheng = lbs = hotweibo = 0
        while True:
            result = requests.get(url)
            if result.status_code == 200:
                content = json.loads(result.content)
                print content
                for result in content['results']:
                    if result['id'] not in mids:
                        mids.append(result['id'])
                    else:
                        self.assertFalse('have same mid')

                    source = result['recommend_source']
                    if source not in (121, 122, 123):
                        self.assertFalse("wrong source")

                    this_score = result['ctr']
                    print "source:%s    score:%s" % (source, this_score)
                    if source in (121, 122):
                        if previous_score != -999:
                            self.assertTrue(previous_score >= this_score)
                        previous_score = this_score
                    if source == 123:
                        if previous_hotweibo_score != -999:
                            self.assertTrue(previous_hotweibo_score >= this_score)
                        previous_hotweibo_score = this_score

                    if source == 121:
                        xiancheng += 1
                    elif source == 122:
                        lbs += 1
                    elif source == 123:
                        hotweibo += 1
            print '鲜城:%s, lbs:%s, 热门微博:%s' % (xiancheng, lbs, hotweibo)
            time.sleep(0.5)


    def testTravel(self):
        mids = []
        uid = '1966695840'
        debug_id = '32233122223'
        province_id = '8008644010000000000'
        previous_score = -999
        previous_hotweibo_score = -999
        url = 'http://172.16.105.69:8080/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=%s&type=6&count=20&detail=true&filter_read=true&debug_id=%s&province_id=%s&domain=5&category=surrounding:travel' % (
            uid, debug_id, province_id)
        xiancheng = lbs = lvyou = hotweibo = 0
        while True:
            result = requests.get(url)
            if result.status_code == 200:
                content = json.loads(result.content)
                print content
                for result in content['results']:
                    if result['id'] not in mids:
                        mids.append(result['id'])
                    else:
                        self.assertFalse('have same mid')

                    source = result['recommend_source']
                    if source not in (131, 132, 133, 134):
                        self.assertFalse("wrong source")

                    this_score = result['ctr']
                    print "source:%s    score:%s" % (source, this_score)
                    if source in (131, 132, 133):
                        if previous_score != -999:
                            self.assertTrue(previous_score >= this_score)
                        previous_score = this_score
                    if source == 134:
                        if previous_hotweibo_score != -999:
                            self.assertTrue(previous_hotweibo_score >= this_score)
                        previous_hotweibo_score = this_score

                    if source == 131:
                        xiancheng += 1
                    elif source == 132:
                        lbs += 1
                    elif source == 133:
                        lvyou += 1
                    elif source == 134:
                        hotweibo += 1
                print '鲜城:%s, lbs:%s, 旅游长文:%s, 热门微博:%s' % (xiancheng, lbs, lvyou, hotweibo)
            time.sleep(0.5)

