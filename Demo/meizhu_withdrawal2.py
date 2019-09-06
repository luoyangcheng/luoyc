from Test.meizhu_withdrawal import withdrawal


class withdrawal2:
    def bc(mobile, password, areaCode, hotel, price,sms):
        session = withdrawal.bb(mobile, password, areaCode,sms)

        data = {'hotel': hotel, 'price': price}

        login_url = "http://192.168.3.19:8090/Home/Withdraw/wechatWithdraw"
        resp2 = session.post(login_url, data)
        print(resp2.content.decode('utf-8'))
