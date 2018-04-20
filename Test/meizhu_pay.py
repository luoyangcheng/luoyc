from Test.meizhu_login import login

class coupons:
    def bc(mobile,password,areaCode,hotel):

        session = login.ll(mobile,password,areaCode)

        data = {'hotel': hotel}

        login_url = "http://192.168.3.19:8090/Home/Withdraw/payRoomNote"
        resp = session.post(login_url, data)
        print ( resp.content.decode('utf-8'))