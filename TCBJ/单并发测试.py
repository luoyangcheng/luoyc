import requests, threading


def n():
    h = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjoibzRUZkZqcFg3NzdPRGpiN3htdUNZQ3lBWFhmdyIsImlhdCI6MTY2NTY0ODkwOCwiZXhwIjoxNjY1NzM1MzA4LCJpc3MiOiJ1c2VyIn0.Q3XHuMQMgvazb3pkC783Ynf45_JaO1L_41ISOrDY0lujvvtf9jb2XK8HLwpMAiC3D8CI_AocN8va8TCN-awKpQ'}
    data = {"giftId": 39, "giftCount": 1, "actProjectId": 130, "deliveryPhone": "18802094078", "deliveryName": "yc", "deliveryProvince": "安徽", "deliveryCity": "安庆", "deliveryCounty": "迎江区", "deliveryStreet": "guangzhou"}
    url = 'https://yyj-test.by-health.com/guidesales/h5/gift/exchangeGift'
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