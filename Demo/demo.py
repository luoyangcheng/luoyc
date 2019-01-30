import hashlib
import requests
import itertools
import json
import datetime


def demo(x, y):
    x = x
    print(x > y + 11 + (x - y - 11) * 0.032)


def md5(data):
    a = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    print(a)


def login():
    mylist = ("".join(x) for x in itertools.product(
        "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        repeat=8))
    for pwd in mylist:
        data = {'mobile': '18802094078', 'password': pwd, 'areaCode': 86}
        login_url = "http://192.168.3.19:8090/Home/Public/login"
        session = requests.Session()
        resp = session.post(login_url, data)
        res = resp.content.decode('utf-8')
        j = json.loads(res)
        code = (j["status"])
        print(pwd, code)
        if code == 200:
            print(code)
            break
        else:
            print(code)
            print(datetime.datetime.now())
            break


# demo(22.04, 10)
# md5("qq111111")
login()
