import requests


def ll(mobile, password, areaCode):
    data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
    login_url = "http://192.168.3.19:8090/Home/Public/login"
    session = requests.Session()
    resp = session.post(login_url, data)
    c = requests.cookies.RequestsCookieJar()
    c.set('cookie-name', 'cookie-value')
    session.cookies.update(c)
    print(resp)
    print(session.cookies.get_dict())


if __name__ == '__main__':
    ll(18802094078, 'qq111111', 86)
