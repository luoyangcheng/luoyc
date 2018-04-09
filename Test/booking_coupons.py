from Test.booking_login import blogin

class coupons:
    def bc(hotel,couponNo):

        session = blogin.bll("18802094078","111111b","86")

        data = {'hotel': hotel ,'couponNo': couponNo}

        login_url = "http://192.168.3.19:8091/Home/Coupon/addUserCoupon"
        resp = session.post(login_url, data)
        print ( resp.content.decode('utf-8'))