#encoding=utf-8
import requests
import time
import hashlib
from bs4 import BeautifulSoup
login_url = 'http://115.29.142.212:8020/Home/Public/login'
link ="http://115.29.142.212:8020/login.html"
s = requests.session()
html = s.get(link).content
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', {'id': 'login-container'})
dataHash = div.get('data-hash')
print(dataHash)
data = {
        "mobile":"13480251015",
        "areaCode":"86",
        "password":"bbc69d27003568a7a94626ce4337bc9d",
        "hash":"5c3d9515c82390c5c66b306598b6b276"
}
# $.md5(n)
mobile = hashlib.md5(data['mobile'].encode('utf8')).hexdigest()

# $.md5(u.password + $.md5(n)) 
pwdMobile = data['password'] + mobile
pwdMobile = hashlib.md5(pwdMobile.encode('utf-8')).hexdigest()

# $.md5(u.password + $.md5(n)) + $("#login-container").data("hash")
pwdMobileHash = pwdMobile+dataHash

# u.hash = $.md5($.md5(u.password + $.md5(n)) + $("#login-container").data("hash"))
data['hash'] = hashlib.md5(pwdMobileHash.encode('utf8')).hexdigest()
print(data['hash'])
a = s.post(login_url,data=data)
print(a.text)