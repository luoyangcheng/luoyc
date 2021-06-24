import requests
import threading
import urllib3
import json

urllib3.disable_warnings()
null = 'null'
token = '#ywzt#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MTkxNTgyMjIsImV4cCI6MTYxOTI0NDYyMiwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMjk0NjgifQ.XNTc8wbzzBF8PByPyMsNhXEgzRYkyoHqxkX01EOJi1F2xwiXxxhydd2sS0Qw6PS0lwfALYzuA-s81eVNCfjeSQ'
productUuid = '4028f55078fd51e90178fd6527bc0008'
url1 = 'https://wx-test1.by-health.com/b2c/rest/consumer/addProductToCart'
data1 = {"header": {"requestId": "94354ae4b24c89b1c8893ca6522bdcf2", "timeStamp": 1612407458743, "applicationId": "b2c-mobile", "ip": "0.0.0.0", "version": "TRIAL", "tokenId": token}, "body": {"unit": 1, "orgNo": "66666662", "isTemp": "1", "type": 1, "productDTO": {"productUuid": productUuid}}}
res = requests.post(url1, verify=False, json=data1)
r = res.content.decode('utf-8')
f = json.loads(r)
shoppingCartUuid = (f["body"]["data"]["shoppingCartUuid"])
data2 = {"header": {"requestId": "1b990e792e3bd93b8b68169becab36aa", "timeStamp": 1612406247115, "applicationId": "b2c-mobile", "ip": "0.0.0.0", "version": "TRIAL", "tokenId": token}, "body": {"actionType": "ADD", "userDTO": {}, "deliveryAddressDTO": {"userDeliveryAddressUuid": 806}, "merchantDTO": {"merchantUuid": "1-1MZNP"}, "deliveryType": "2", "memo": "", "shoppingCartUuidList": [shoppingCartUuid], "clerkId": "", "liveRoomId": null, "deliveryProvince": "广东", "deliveryCity": "广州", "deliveryArea": "天河区", "deliveryStreet": "测试", "deliveryName": "测试", "deliveryContactNo": "18802094078", "deliveryZipcode": "测试", "orderType": "3"}}
url2 = 'https://wx-test1.by-health.com/b2c/rest/consumer/changeOrder'


def tixian():
    resp = requests.post(url2, verify=False, json=data2)
    print(resp.content.decode('utf-8'))


t1 = threading.Thread(target=tixian)
t2 = threading.Thread(target=tixian)

if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
