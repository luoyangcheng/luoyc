import requests
from time import ctime

class login:
    def ll(mobile,password,areaCode):
        data = {'mobile': mobile,
                'password': password,
                'areaCode': areaCode}

        login_url = "http://192.168.3.19:8090/Home/Public/login"

        session = requests.Session()

        resp = session.post(login_url, data)
        print ( resp.content.decode('utf-8'))
        return session
