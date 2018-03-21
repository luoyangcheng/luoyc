#encoding=utf-8
import requests
import urllib.request,urllib.parse.urllib.error
import http.cookiejar
login_url = "http://115.29.142.212:8020/mobile/user/login"
data = {"areaCode":"86","account":"13480251015",
        "passwd":'''PmB63By77hCrBpaq0oAIS03BOMZu9dFahAV3hu+U4wpgl+YhlGUoCIPKJ9WZsQJYHmdJTe6yYdq+
5Tg+lEEXXMyS6xPO+KRvuLadi84InZzBznmwN96NZ3eH3FC7kjKNYp2c5Sp57P06cCMdPgzRFu0+
S1UK4IRb+WMiyqkSFzdo/UU4qnxIb66i3oqGoGdrA8z/AmWBOFybxwUjPTEe6Xz5ypxU7vvFtI2i
szwd53vbMT/12nibrtpNhbr6hZYdxMY5M91u5XUPaV+ilMtUP2hFKEjnOm0Hzr3A6yxrxEBnjzEw
bEnSq106LDyX6RH05dnmMw38eM7FrZeLePs/YQ=='''}
postdata = urllib.parse.urlencode(data).encode()
header = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencode;charset=uft-8'}
cookie_filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(login_url,postdata,header)
try:
    response = opener.open(request)
    page = response.read().decode()
    # print(page)
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
print(cookie)
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)
