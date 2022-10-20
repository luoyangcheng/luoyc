import time
import requests

current = int(time.time() * 1000)
print(current)
data = {"guid": "1721C5D2-17F0-440A-9DBD-5BFC76A0CBE4", "reqId": current, "jsonInfo": {"actType": "LOTTERY", "orderId": 2581057, "memberId": 20, "createTime": current, "uploadTime": "2022-08-25T06:34:01.990Z", "mobilePhone": "13246492686", "totalPoints": 1000, "presentLegalLevel": 0}}
r = requests.post("http://172.16.8.88:6581/services/v1/upload", json=data, verify=False)
print(r.content.decode('utf-8'))
print(r.status_code)