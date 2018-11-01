import requests


class Meizhu_login:
    def login(mobile, password, areaCode):
        data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
        login_url = "http://192.168.3.19:8090/Home/Public/login"
        session = requests.Session()
        result = session.post(login_url, data)
        return session, result
