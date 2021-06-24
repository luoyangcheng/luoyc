import requests
import threading
import urllib3

urllib3.disable_warnings()
null = 'null'
token = ''
productUuid = ''
url1 = 'https://yyj-test.by-health.com/scrm/liteActivity/exchangePrize'
header = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MjA5NjA0OTgsImV4cCI6MTYyMTA0Njg5OCwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMjk0NjgifQ.hQrsdDg0KCmNdMjr_k3xeJVoJ2PQ4nfx6u5Uznz2Nw3czpWt0GKPI_w3KJcEGVpjsZX--OOofrJSUTaTzKzgvg'}
data1 = {"openId": "o-DCM5R2HsZXqzU7TTTk-IYseSlE", "actId": "320", "prizeId": 2, "amount": 1}
#  res = requests.post(url1, verify=False, json=data1, headers=header)
#  r = res.content.decode('utf-8')


def tixian():
    resp = requests.post(url1, verify=False, json=data1, headers=header)
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
