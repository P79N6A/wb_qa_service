import os
import urllib
import urllib2

import requests


url = '10.210.130.44:10002/rpc/DslShellService/Query'
body = 'dsl:"(term distance:"1042:user_00001" vertical:mblog_list_test order:-sphere_distance(place_user.lon,place_user.lat,0.1,0.1,6371004) limit:3 select:place_user.lon,place_user.lat)"'

# resp = requests.post(url, data=body)
# print resp.content
#
# output = os.popen('curl -d ' + body + ' url')
# out = output.read()
# print out

# req = urllib2.Request(url)
# data = urllib.urlencode(body)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor)
# response = opener.open(req, data)
# print response.read()


import commands
cmd = '''curl -d 'dsl:"(term distance:\"1042:user_00001\" vertical:mblog_list_test order:-sphere_distance(place_user.lon,place_user.lat,0.1,0.1,6371004) limit:3 select:place_user.lon,place_user.lat)"'  http://10.210.130.44:10002/rpc/DslShellService/Query'''
result = commands.getstatusoutput(cmd)
output = result[1]
print output