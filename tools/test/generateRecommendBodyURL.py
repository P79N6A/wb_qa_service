#encoding:utf-8
import random

def generate(f):
    citys = ['8008611000000000000', '8008612000000000000', '8008613010000000000', '8008613090000000000', '8008651010000000000', '8008641110000000000', '8008641010000000000']
    uid = 1000000000
    debug_id = random.randint(1000000000, 9999999999)
    i = random.randint(0, 6)
    url = '/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=%s&type=6&count=20&detail=false&filter_read=true&debug_id=%s&category=surrounding:hot&province_id=%s' % (uid, debug_id, citys[i])
    print url
    f.write(url + '\n')


if __name__ == '__main__':
    k = 1000000
    with open('surrounding', 'w') as f:
        while k > 0:
            generate(f)
            k -= 1
