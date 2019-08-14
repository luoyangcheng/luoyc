#encoding=utf-8
import requests
url = 'http://115.29.142.212:8020/Home/Public/login'
data ={
        "mobile":"13480251015",
        "areaCode":"86",
        "password":"bbc69d27003568a7a94626ce4337bc9d",
        "hash":"5c3d9515c82390c5c66b306598b6b276"
}
r = requests.post(url,data=data)
print(r.cookies)
print(requests.utils.dict_from_cookiejar(r.cookies))