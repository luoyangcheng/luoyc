import requests
import threading
import urllib3

urllib3.disable_warnings()
null = 'null'
token = ''
productUuid = ''
url1 = 'https://wx-test1.by-health.com/scrmv2/antifakecode/antifakecodeIntegral'
header = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MTgxOTEzMjEsImV4cCI6MTYxODI3NzcyMSwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMjk0NjgifQ.sRDX_Jd_KDgzrLTNzfyQr1Mbjoixodh1zbtEdX06E_whNiq4v9MjdMSAwHl-N_ZYCOaOJIDqEFSNHoep39tpcQ'}
data1 = {"storeId": "1-WAYZ2", "channelType": 4, "mobilePhone": "15278427701", "antifakecode": "6731284330296179", "clerkId": "", "comment": "微信礼品商城首页积分", "brand": "TCBJ"}
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
