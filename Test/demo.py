import requests
import urllib3
import json


urllib3.disable_warnings()  # 忽略警告
data1 = {"header": {"requestId": "94354ae4b24c89b1c8893ca6522bdcf2", "timeStamp": 1612407458743, "applicationId": "b2c-mobile", "ip": "0.0.0.0", "version": "TRIAL", "tokenId": "#ywzt#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MTIzMjU4NDUsImV4cCI6MTYxMjQxMjI0NSwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMjkxMjcifQ.8o0TrsGYJphrR8kpN-wTOc92BovMdCAV2vI9rxvAYJ5wbm7xyFeok37f5_zzbZsRvWNyaJGv0peu4_DM7-MXGQ"}, "body": {"unit": 1, "orgNo": "66666662", "isTemp": "1", "type": 1, "productDTO": {"productUuid": "4028f5507768d44501776ae5581d002a"}}}
url1 = 'https://wx-test1.by-health.com/b2c/rest/consumer/addProductToCart'
res = requests.post(url1, verify=False, json=data1)
r = res.content.decode('utf-8')
f = json.loads(r)
token = (f["body"]["data"]["shoppingCartUuid"])
print(token)