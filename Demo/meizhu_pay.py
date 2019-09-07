from Test.meizhu_login import login


class coupons:
    def bc(mobile, password, areaCode, hotel):
        session = login.ll(mobile, password, areaCode)

        data = {'hotel': hotel}

        login_url = "http://192.168.100.104:12306/login/doLogin?account=luoyc&password=qq111111"
        resp = session.post(login_url, data)
        print(resp.content.decode('utf-8'))


if __name__ == "__main__":
    coupons.bc('luoyc', 'qq111111')
