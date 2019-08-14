#encoding=utf-8
import requests
data = {"areaCode":"86","account":"13480251015",
        "passwd":'''PmB63By77hCrBpaq0oAIS03BOMZu9dFahAV3hu+U4wpgl+YhlGUoCIPKJ9WZsQJYHmdJTe6yYdq+
5Tg+lEEXXMyS6xPO+KRvuLadi84InZzBznmwN96NZ3eH3FC7kjKNYp2c5Sp57P06cCMdPgzRFu0+
S1UK4IRb+WMiyqkSFzdo/UU4qnxIb66i3oqGoGdrA8z/AmWBOFybxwUjPTEe6Xz5ypxU7vvFtI2i
szwd53vbMT/12nibrtpNhbr6hZYdxMY5M91u5XUPaV+ilMtUP2hFKEjnOm0Hzr3A6yxrxEBnjzEw
bEnSq106LDyX6RH05dnmMw38eM7FrZeLePs/YQ=='''}
header = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencode;charset=uft-8'}
conn = requests.session()
r = conn.post("http://115.29.142.212:8020/mobile/user/login",data=data)
# print(r.request.headers)
print(r.cookies)
cookies_data = requests.utils.dict_from_cookiejar(r.cookies)
print(cookies_data)
# data = {"cname":"接口测试创建集群-有为",
#         "universalTime":"5",
#         "desc":"333",
#         "type":"1",
#         "addr":"11",
#         "cont":"联系人",
#         "phone":'13480251015',
#         "areaCode":"1"
#         }
# req = conn.post("http://115.29.142.212:8020/Home/Community/create",cookies=r.cookies,data=data)
# # print(req.request.headers)
# # print(req.cookies)