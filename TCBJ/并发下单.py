import requests
import threading
import urllib3
import json

urllib3.disable_warnings()
null = 'null'
token = '#ywzt#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NDE0MzgwMDAsImV4cCI6MTY0MTUyNDQwMCwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMzI0NzgifQ.vgS-ZxZ25FdW7696MgBoRLH-cql4RYDLn9Hv7Wwf0Qxw2rh2M-ckhJpbhEBnGlmXqf7f0mpTt-bCdv1gJAMvrA'
productUuid = '4028f5507de64fd5017e04511dd1001c'
url1 = 'https://wx-test1.by-health.com/b2c/rest/consumer/addProductToCart'
data1 = {"header": {"requestId": "94354ae4b24c89b1c8893ca6522bdcf2", "timeStamp": 1612407458743, "applicationId": "b2c-mobile", "ip": "0.0.0.0", "version": "TRIAL", "tokenId": token}, "body": {"unit": 1, "orgNo": "66666662", "isTemp": "1", "type": 1, "productDTO": {"productUuid": productUuid}}}
res = requests.post(url1, verify=False, json=data1)
r = res.content.decode('utf-8')
f = json.loads(r)
print(f)
shoppingCartUuid = (f["body"]["data"]["shoppingCartUuid"])
data2 = {"header":{"requestId":"c6135ce2278f1799a13cb035b41e5aed","timeStamp":1641440371589,"applicationId":"b2c-mobile","ip":"0.0.0.0","version":"TRIAL","tokenId":"#ywzt#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NDE0MzgwMDAsImV4cCI6MTY0MTUyNDQwMCwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMzI0NzgifQ.vgS-ZxZ25FdW7696MgBoRLH-cql4RYDLn9Hv7Wwf0Qxw2rh2M-ckhJpbhEBnGlmXqf7f0mpTt-bCdv1gJAMvrA"},"body":{"actionType":"ADD","userDTO":{},"deliveryAddressDTO":{"userDeliveryAddressUuid":938},"merchantDTO":{"merchantUuid":"1-1MZNP"},"deliveryType":"1","memo":"","shoppingCartUuidList":[shoppingCartUuid],"clerkId":"","liveRoomId":null,"deliveryProvince":"安徽","deliveryCity":"安庆","deliveryArea":"迎江区","deliveryStreet":"测试一下","deliveryName":"咯咯哒","deliveryContactNo":"18802094078","deliveryZipcode":"","saleType":"specialSale","openId":"o-DCM5R2HsZXqzU7TTTk-IYseSlE"}}
url2 = 'https://wx-test1.by-health.com/b2c/rest/consumer/changeOrder'


def tixian():
    resp = requests.post(url2, verify=False, json=data2)
    print(resp.content.decode('utf-8'))


t1 = threading.Thread(target=tixian)

if __name__ == '__main__':
    t1.setDaemon(True)
    t1.start()
    t1.join()
