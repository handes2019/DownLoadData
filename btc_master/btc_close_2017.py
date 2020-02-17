from __future__ import (absolute_import, division, print_function, unicode_literals)

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

try:
    # Python 2.x 版本
    from urllib2 import urlopen
except ImportError:
    # Python 3.x 版本
    from urllib.request import urlopen
import json
import requests

json_url = 'https://github.com/handes2019/DownLoadData/blob/master/btc_master/btc_close_2017.json'
response = urlopen(json_url)
#读取数据
req = response.read()

with open('btc_close_2017.json') as f:
    req = f.read()

#将数据写入文件
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)


req = requests.get(json_url)
file_request = req.json()
with open('btc_close_2017_urllib.json', 'w', encoding='utf-8') as f:
    f.write(req.text)
#加载json格式
file_urllib = json.loads(req)
print(file_urllib == file_request)