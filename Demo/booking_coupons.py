from booking_login import blogin


class coupons:
    def bc(mobile, password, areaCode, hotel, couponNo):

        session = blogin.bll(mobile, password, areaCode)

        data = {'hotel': hotel, 'couponNo': couponNo}

        login_url = "http://192.168.3.19:8091/Home/Coupon/addUserCoupon"
        resp = session.post(login_url, data)
        print(resp.content.decode('utf-8'))
