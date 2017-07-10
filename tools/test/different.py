import json
import requests
import time

temp_list = []
same_list = ['4035265624267306', '4035307441121598', '4035157637351773', '4035245936710064']

def write_surround():
    print len(temp_list)
    with open('surround_mid', 'w') as f:
        debug_id = '212151211227009'
        surround_url = 'http://172.16.105.69:8080/2/recommendation/general_recommend_category.json?test_environment=true&source=646811797&uid=1000000003&type=6&count=20&detail=false&filter_read=true&debug_id=%s&category=surrounding:hot&province_id=8008611000000000000' % debug_id
        while True:
            response = requests.get(surround_url)
            content = response.content
            print content
            json_content = json.loads(content)
            print json_content
            for sing in json_content['results']:
                if 'id' in sing:
                    mid = sing['id'].strip()
                    print mid
                    f.write(mid + '\n')

                    if str(mid) in same_list:
                        print mid

                else:
                    break
            time.sleep(0.5)

def write_body():
    print len(temp_list)
    with open('same', 'w') as same_f:
        with open('body_mid', 'w') as f:
            debug_id = '99222233442323'
            body_uirl = 'http://172.16.105.69:8080/2/recommendation/general_recommend_body.json?test_environment=true&source=646811797&uid=1966695840&type=6&count=15&detail=true&filter_read=true&debug_id=%s&id=4034830049877872' % debug_id
            while True:
                response = requests.get(body_uirl)
                content = response.content
                print content
                json_content = json.loads(content)
                print json_content
                for sing in json_content['results']:
                    if 'id' in sing:
                        mid = sing['id'].strip()

                        # if str(mid) != '4034874295455618':
                        #     continue
                        # else:
                        #     print '-----'

                        print mid
                        f.write(mid + '\n')
                        if mid in temp_list:
                            same_f.write(mid + '\n')
                        if str(mid) in same_list:
                            print mid
                    else:
                        break
                time.sleep(0.5)


def readRecommend():
    print len(temp_list)
    with open('same_new1', 'w') as same_f:
        with open('recommend_mid', 'w') as f:
            debug_id = '43534537777'
            recom_url = 'http://172.16.105.69:8080/2/recommendation/general_recommend.json?test_environment=true&source=646811797&uid=1966695840&type=6&count=20&detail=false&filter_read=true&debug_id=%s' % debug_id
            while True:
                response = requests.get(recom_url)
                content = response.content
                print content
                json_content = json.loads(content)
                print json_content
                for sing in json_content['results']:
                    if 'id' in sing:
                        mid = sing['id'].strip()
                        print mid
                        f.write(mid + '\n')
                        if mid in temp_list:
                            same_f.write(mid + '\n')
                        if str(mid) in same_list:
                            print mid
                    else:
                        break
                time.sleep(0.5)

    # debug_id = '666666667'
    # recom_url = 'http://172.16.105.69:8080/2/recommendation/general_recommend.json?test_environment=true&source=646811797&uid=1966695840&type=6&count=20&detail=false&filter_read=false&debug_id=%s' % debug_id
    # while True:
    #     response = requests.get(recom_url)
    #     content = response.content
    #     print content
    #     json_content = json.loads(content)
    #     print json_content
    #     for sing in json_content['results']:
    #         if 'id' in sing:
    #             mid = sing['id'].strip()
    #             if str(mid) == '4034906306333330':
    #                 print 'recommend has mid %s' % mid

if __name__ == '__main__':
    # with open('surround_mid', 'r') as ff:
    #     while True:
    #         line = ff.readline()
    #         print line
    #         if not line:
    #             break
    #         else:
    #             temp_list.append(line.strip())
    write_body()

    # write_surround()

    # readRecommend()




    # with open('common', 'r') as ff:
    #     while True:
    #         line = ff.readline()
    #         print line
    #         if not line:
    #             break
    #         else:
    #             temp_list.append(line.strip())
    #     write_body()