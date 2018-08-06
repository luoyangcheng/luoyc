import requests
# from time import ctime


class blogin:
    def bll(mobile, password, areaCode):
        data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}

        # 设置请求头
        # headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

        # 登录时表单提交到的地址（登录接口）
        login_url = "http://192.168.3.19:8091/Home/Public/login"

        # 构造Session
        session = requests.Session()

        # 在session中发送登录请求，此后这个session里就存储了cookie
        # 可以用print(session.cookies.get_dict())查看
        resp = session.post(login_url, data)
        print(resp.content.decode('utf-8'))
        return session