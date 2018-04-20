from Test.meizhu_login import login


class withdrawal:
    def bb(mobile, password, areaCode,sms):
        session = login.ll(mobile, password, areaCode)

        data2 = {'vcode':sms}

        sms_url = 'http://192.168.3.19:8090/Home/Account/verifyWithMobile'

        resp1 =session.post(sms_url,data2)
        print(resp1.content.decode('utf-8'))
        return session

