# appId = 'FDA1276694626DA0'
# appSecret = 'B8FFCF23FDA1276694626DA0E228C6FA'
# timestamp = '20190417120505'
# nonce = "appId=" + appId + "&appSecret=" + appSecret + "&timestamp=" +  timestamp
# print(nonce)
#
# import requests
#
# r = requests.post(
#     url='http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',
#     data={'cityId':438})
# print(r.json())
import unittest
import json
import requests

#
base_url = "https://app-uat.maxxipoint.com/api/newProduct/doSupport"
payload = "{\"bizContent\":\"{'memberId':'1421381708','contentId':'9635','supportType':'1'}\"," \
                   "\"devContent\":\"{'appIdentify':'com.maxxipoint.iosTest','" \
                   "deviceId':'35ad6e2bb310c564b0eff4715d07f83adbedb33d','deviceModel':'iPhone 8'," \
                   "'appVersion':'5.5.0','deviceVersion':'12.1.2','platform':'iOS'}\"}"
header = {
             'requestid': "2122",
             'appid': "APPKHFJJ78897FH",
             'timestamp': "20190129090320",
             'reqtype': "app",
             'tokenid': "3F1C2083CD8FD7F6CF5D6062C9E6871723EAB325",
             'content-type': "application/json",
             'cache-control': "no-cache",
             'postman-token': "72919a71-eace-30a0-e163-f743965ff2a2"
         }
r = requests.post(base_url, headers=header, data=payload)
result = r.json()['data']['country']
print(result)
# assertEqual(result['data'], '{"respCode":"00","respMsg":"成功","bizData":'
#                                                '"{\\"supportNum\\":\\"101\\"}",'
#                                                '"respDate":"20190123","respTime":"180310"}')
# assertEqual(result['message'], '成功')


import requests
请求地址
url = "https://api.global.net/datastore/v1/tracks/" + trackId + "?location=12}"
# 发送get请求
r = requests.get(url)
# 获取返回的json数据
print(r.json())
