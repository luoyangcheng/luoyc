import requests


class login:
    def ll(mobile, password, areaCode):
        data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}

        login_url = "http://192.168.3.19:8090/Home/Public/login"

        session = requests.Session()
        # session = requests.cookies()

        resp = session.post(login_url, data)
        print(resp.content.decode('utf-8'))
        return session
