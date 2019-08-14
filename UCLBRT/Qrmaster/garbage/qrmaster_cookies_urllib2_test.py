#encoding=utf-8
#https://www.cnblogs.com/meitian/p/4607737.html
import requests
import urllib
import http.cookiejar
login_url = 'http://115.29.142.212:8020/Home/Public/login'
data ={
        "mobile":"13480251015",
        "areaCode":"86",
        "password":"bbc69d27003568a7a94626ce4337bc9d",
        "hash":"5c3d9515c82390c5c66b306598b6b276"
}
header = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencode;charset=uft-8'}
postdata = urllib.parse.urlencode(data).encode("utf-8")
print(postdata)
req = urllib.request.Request(login_url,postdata,header)
#urlresponse = urllib.request.urlopen(req).read().decode('utf-8')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)
print(r.read().decode('utf-8'))
