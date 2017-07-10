#encoding:utf-8
import json

import requests
import time


if __name__ == '__main__':

    all_mids = []
    all_count = 0
    citys = ['8008611000000000000', '8008612000000000000', '8008613010000000000', '8008613090000000000', '8008651010000000000', '8008641110000000000', '8008641010000000000']
    i = 0

    while True:
        url = 'http://localhost:8081/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=1966688888&type=6&count=20&detail=false&filter_read=true&debug_id=123&domain=3&category=surrounding:hot&province_id=' + citys[i]
        result = requests.get(url)
        if result.status_code != 200:
            print 'error %s' % (result.status_code)

        res = json.loads(result.content)['results']

        if len(res) <= 5:
            i = i + 1
            if i == 7:
                print 'end'
                break
            print 'change city %s' % (citys[i])

        if res:
            all_count = all_count + len(res)
            print all_count
            for o in res:
                # print o["id"]
                if o["id"] in all_mids:
                    print '%s already exists' % (o["id"])
                else:
                    all_mids.append(o["id"])

        time.sleep(1)
