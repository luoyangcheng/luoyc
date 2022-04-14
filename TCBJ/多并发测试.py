import threading
import requests
from collections import Counter


def ll(i, N):
    h = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJJZCI6MjEsInRlbmFudElkIjoxLCJyb2xlTGV2ZWwiOjEsImlhdCI6MTY0NzM5NDYwMCwiZXhwIjoxNjQ3NDgxMDAwLCJpc3MiOiJzdHVkZW50In0.UNd0v0gKvXzmcj7K6ZTNNfgKd66hMt-qqPOk0nffPVNf6Z33-6pwVu_UmJb7WbJEr0gRqdSsLebQcIrzmx1wxA'}
    data = {"adminId": 4, "orgNo": "183671", "gender": "女", "phone": "18802094081", "validateCode": "7474", "name": "罗兰", "planId": 1, "profiles": {"profile1": {"policyPic": "https://upload-yyj.by-health.com/upload/images/0329105322819.png", "orgName": "130分店", "TRIG": 1.8, "TCHOL": 5.18, "HDL-CH": 1.08, "LDL-CH": 3.9, "age": "12", "report": ["https://upload-yyj.by-health.com/upload/images/0329105328840.png"], "memberLabel": ["高血脂"]}}}
    url = 'https://yyj-test.by-health.com/his/plan/h5/memberLoginByMsg'
    resp = requests.post(url, json=data, headers=h)
    status = resp.status_code
    if status == 200:
        print(resp.content.decode('utf-8'))
    elif status != 200:
        print(resp.content.decode('utf-8'))
    # print(i, '请求状态:', status, '请求耗时：', seTime / 1000000)
    N.append(status)


T = []
N = []
for i in range(0, 5):
    t1 = threading.Thread(target=ll, args=(i, N))
    T.append(t1)

if __name__ == '__main__':
    for i in T:
        i.setDaemon(True)
        i.start()
    for j in T:
        j.join()
    print(Counter(N))
