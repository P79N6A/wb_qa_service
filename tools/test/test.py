import random

with open('body', 'w') as f:
    for i in xrange(50):
        with open('recommend_body', 'r') as file:
            while True:
                line = file.readline()
                if line:
                    temp = line.strip().split('&id=')
                    mid = temp[1]
                    debug_id = random.randint(1000000000, 9999999999)
                    url_prefix = '/2/recommendation/general_recommend_body.json?domain=5&test_environment=true&source=646811797&uid=1966695840&type=6&count=15&detail=true&filter_read=true&debug_id=%s&id=' % debug_id
                    url_body = url_prefix + mid
                    f.write(url_body + '\n')
                else:
                    break