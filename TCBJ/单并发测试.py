import requests, threading


def n():
    h = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJJZCI6MjEsInRlbmFudElkIjoxLCJyb2xlTGV2ZWwiOjEsImlhdCI6MTY0NzM5NDYwMCwiZXhwIjoxNjQ3NDgxMDAwLCJpc3MiOiJzdHVkZW50In0.UNd0v0gKvXzmcj7K6ZTNNfgKd66hMt-qqPOk0nffPVNf6Z33-6pwVu_UmJb7WbJEr0gRqdSsLebQcIrzmx1wxA'}
    data = {"adminId": 4, "orgNo": "183671", "gender": "女", "phone": "18802094081", "validateCode": "7474", "name": "罗兰", "planId": 1, "profiles": {"profile1": {"policyPic": "https://upload-yyj.by-health.com/upload/images/0329105322819.png", "orgName": "130分店", "TRIG": 1.8, "TCHOL": 5.18, "HDL-CH": 1.08, "LDL-CH": 3.9, "age": "12", "report": ["https://upload-yyj.by-health.com/upload/images/0329105328840.png"], "memberLabel": ["高血脂"]}}}
    url = 'https://yyj-test.by-health.com/his/plan/h5/memberLoginByMsg'
    res = requests.post(url, json=data, headers=h)
    r = res.content.decode('utf-8')
    print(r)


t1 = threading.Thread(target=n)
t2 = threading.Thread(target=n)

if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()