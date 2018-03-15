import requests
import sys
import io
class login:
    def __init__(self,mobile,password,areaCode):
        self.mobile=mobile
        self.password=password
        self.areaCode=areaCode
        data = {'mobile': self.mobile,
                'password': self.password,
                'areaCode': self.areaCode}

        # 设置请求头
        # headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

        # 登录时表单提交到的地址（登录接口）
        login_url = "http://115.29.142.212:8010/Home/Public/login"

        # 构造Session
        session = requests.Session()

        # 在session中发送登录请求，此后这个session里就存储了cookie
        # 可以用print(session.cookies.get_dict())查看
        resp = session.post(login_url, data)
        print ( resp.content.decode('utf-8'))
    def f(self,s):
        self.s=s
        session = requests.Session()
        return session
