import requests
import hashlib
from bs4 import BeautifulSoup

login_url = 'http://192.168.3.19:8082/login.html'
login_api = "http://192.168.3.19:8082/Home/Public/login"

data = {
    'mobile': '18802094078',
    'password': '45101b093c4e8acf32a525dc231afd50',
    'areaCode': '86'
}


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
    print(hash)
    gethash(data, hash)
    print(data['hash'])
    a = session.post(login_api, data=data)
    print(a.text)
