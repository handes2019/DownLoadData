from __future__ import (absolute_import, division, print_function, unicode_literals)



try:
    # Python 2.x 版本
    from urllib2 import urlopen
except ImportError:
    # Python 3.x 版本
    from urllib.request import urlopen
import json
import requests


#####   1
# json_url = 'https://github.com/handes2019/DownLoadData/blob/master/btc_master/btc_close_2017.json'
# response = urlopen(json_url)
# #读取数据
# req = response.read()
#
# # with open('btc_close_2017.json') as f:
# #     req = f.read()
#
# #将数据写入文件
# with open('btc_close_2017_urllib.json', 'wb') as f:
#     f.write(req)
#
#
# req = requests.get(json_url)
# file_request = req.json()
# with open('btc_close_2017_urllib.json', 'w', encoding='utf-8') as f:
#     f.write(req.text)
# #加载json格式
# file_urllib = json.loads(req)
# print(file_urllib == file_request)

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
#打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))
