import requests
import threading
import urllib3
import json

urllib3.disable_warnings()
null = 'null'
token = '#ywzt#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NTQwNjMxNzAsImV4cCI6MTY1NDE0OTU3MCwiaXNzIjoiTWVtYmVyIiwic3ViIjoiMTE0In0.6ChDc_Aaf6I1_cT8j7bMGHI_3TBHVDAzUmJhGUu20e5vHaGhWYYnc3xrefkukHiHyi4pw6wbKwWrnuDLuVr10w'
productUuid = '4028f550811e60c301811e71f6870006'
url1 = 'https://wx-test1.by-health.com/b2c/rest/consumer/addProductToCart'
data1 = {"header": {"requestId": "7d3f69582ec6639165baa82ea85c2d43", "timeStamp": 1654073224744, "applicationId": "b2c-mobile", "ip": "0.0.0.0", "version": "TRIAL", "tokenId": token}, "body": {"unit": 1, "orgNo": "331111", "isTemp": "1", "type": 1, "posterId": "1\t", "productDTO": {"productUuid": productUuid}}}
res = requests.post(url1, verify=False, json=data1)
r = res.content.decode('utf-8')
f = json.loads(r)
print(f)
shoppingCartUuid = (f["body"]["data"]["shoppingCartUuid"])
print(shoppingCartUuid)
data2 = {
    "header": {
        "requestId": "128c5ec36a9154ead4e4c6713e88814b",
        "timeStamp": 1654073249121,
        "applicationId": "b2c-mobile",
        "ip": "0.0.0.0",
        "version": "TRIAL",
        "tokenId": token
    },
    "body": {
        "actionType": "ADD",
        "userDTO": {},
        "deliveryAddressDTO": {
            "userDeliveryAddressUuid": 35
        },
        "merchantDTO": {
            "merchantUuid": "1-101C5S8"
        },
        "deliveryType": "2",
        "memo": "",
        "shoppingCartUuidList": [shoppingCartUuid],
        "clerkId": "",
        "liveRoomId": null,
        "deliveryProvince": "广东",
        "deliveryCity": "广州",
        "deliveryArea": "黄埔区",
        "deliveryStreet": "科汇金谷",
        "deliveryName": "罗扬成",
        "deliveryContactNo": "18802094078",
        "deliveryZipcode": "",
        "saleType": "specialSale",
        "openId": "o-DCM5R2HsZXqzU7TTTk-IYseSlE",
        "isFlagShip": "false",
        "useCouponDTO": {
            "couponUuid": "4028f550811d676101811d7857f5000c",
            "userCouponUuid": "4028f239811dcc2401811dd93f960006"
        }
    }
}
url2 = 'https://wx-test1.by-health.com/b2c/rest/consumer/changeOrder'


def tixian():
    resp = requests.post(url2, verify=False, json=data2)
    # print(resp.content.decode('utf-8'))


t1 = threading.Thread(target=tixian)
t2 = threading.Thread(target=tixian)

if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
