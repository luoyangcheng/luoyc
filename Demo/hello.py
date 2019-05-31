import requests


def login(areaCode, account, passwd):
    data1 = {'areaCode': areaCode, 'account': account, 'passwd': passwd}
    login_url = "http://qrm.uclbrt.com/mobile/user/login"

    session = requests.Session()
    resp = session.post(login_url, data1)
    r = resp.content.decode('utf-8')
    print(r)


if __name__ == '__main__':
    login(86, 18802094078, 'qq111111')
