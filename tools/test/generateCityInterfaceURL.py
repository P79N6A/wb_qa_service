#encoding:utf-8

import random
import unittest

city_list = []

class generateCityURLs(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        with open('source/citys', 'r') as file:
            lines = file.readlines()
            for line in lines:
                pro_id = line.split()[3]
                if line.index(line) <= 360:
                    for i in xrange(100):
                        city_list.append(pro_id)
                else:
                    city_list.append(pro_id)
        random.shuffle(city_list)

    def testCity(self):
        count = 1000000
        i = 0
        with open('city_travel', 'w') as f:
            while i < count:
                i += 1
                uid = '1966695840'
                debug_id = random.randint(1000000000, 9999999999)
                province_id = city_list[random.randint(0, len(city_list) - 1)]
                request_category = 'surrounding:travel'
                url = '/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=%s&type=6&count=20&detail=true&filter_read=true&debug_id=%s&domain=5&province_id=%s&category=%s' % (
                uid, debug_id, province_id, request_category)
                print url
                f.write(url + '\n')
