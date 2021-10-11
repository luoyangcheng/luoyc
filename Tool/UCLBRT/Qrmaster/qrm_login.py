import requests
import hashlib
from bs4 import BeautifulSoup

login_url = 'http://192.168.3.19:8082/login.html'
login_api = "http://192.168.3.19:8082/Home/Public/login"


def getdata(mobile, password, areaCode):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    password = md5.hexdigest()
    data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
    return data


def md5(str):
    m = hashlib.md5(str.encode("utf-8"))
    return m.hexdigest()


def hash(url):
    soup = BeautifulSoup(session.get(login_url).text, 'html.parser')
    course = soup.find_all('div', class_="card")
    for i in course:
        hash = i['data-hash']
    return hash


def gethash(data, hash):
    mobile_pwd = md5(data['password'] + md5(data['mobile']))
    mobile_pwd_hash = mobile_pwd + hash
    data['hash'] = md5(mobile_pwd_hash)


if __name__ == "__main__":
    session = requests.session()
    hash = hash(login_url)
    data = getdata('18802094078', 'qq111111', '86')
    print(hash)
    gethash(data, hash)
    print(data['hash'])
    a = session.post(login_api, data=data)
    print(a.text)
