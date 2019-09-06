import requests
import json
import re
from Open_Excel import read_excel, write_excel,update_excel


def login():
    data = {'flag': 1, 'username': 'luoyc', 'password': 'qq111111'}
    h = {'Upgrade-Insecure-Requests': '1', 'Content-Type': 'application/x-www-form-urlencoded'}
    login_url = "http://192.168.100.108/cas/login.aspx"
    session = requests.Session()
    resp = session.post(login_url, data=data, headers=h, allow_redirects=False)  #单点登陆要禁止重定向
    result = resp.content.decode('utf-8')
    SetCookie = resp.headers.get('Set-Cookie')
    vt = re.findall(r"vt=(.+?);", SetCookie)
    return vt[0]


def inhospital():
    excel_path = "../AID/Search/case.xlsx"
    vt = login()
    Headers = {'Authorization': vt}
    url = 'http://192.168.100.104:12306/es-search/inhospital'
    update_excel(excel_path, '住院')
    true = 'true'
    null = 'null'
    false = 'false'
    Test_data = []
    for i in range(2, 4):
        one_data = read_excel(excel_path, '住院', i)
        Test_data.append(one_data)
    actual = []
    for x, y in zip(Test_data[0], Test_data[1]):
        c = json.loads(x)
        resp = requests.post(url, json=c, headers=Headers)
        r = resp.content.decode('utf-8')
        print(r)
        f = json.loads(r)
        try:
            num = (f["data"]["total"])
        except Exception as e:
            msg = (f["msg"])
            code = (f["code"])
            if msg == '执行成功' and code == 200:
                num = 0
            else:
                print("该节点出错了！")
        if num == y:
            actual.append(num)
        else:
            actual.append(num)
    write_excel(excel_path, '住院', actual)


def clinic():
    excel_path = "../AID/Search/case.xlsx"
    vt = login()
    Headers = {'Authorization': vt}
    url = 'http://192.168.100.104:12306/es-search/clinic'
    update_excel(excel_path, '门诊')
    true = 'true'
    null = 'null'
    false = 'false'
    Test_data = []
    for i in range(2, 4):
        one_data = read_excel(excel_path, '门诊', i)
        Test_data.append(one_data)
    actual = []
    for x, y in zip(Test_data[0], Test_data[1]):
        c = json.loads(x)
        resp = requests.post(url, json=c, headers=Headers)
        r = resp.content.decode('utf-8')
        print(r)
        f = json.loads(r)
        num = (f["data"]["total"])
        if num == y:
            actual.append(num)
        else:
            actual.append(num)
    write_excel(excel_path, '门诊', actual)


if __name__ == "__main__":
    x = input('运行住院请输入：1，运行门诊请输入：2\n')
    if x == '1':  
        inhospital()
    elif x == '2':
        clinic()
    else:
        print('输入错误！')
