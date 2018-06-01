import requests, hashlib
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

login_url = 'http://115.29.142.212:8020/login.html'
login_api = 'http://115.29.142.212:8020/Home/Public/login'
addroom_url = 'http://115.29.142.212:8020/Home/Room/addRooms'
user_url = 'http://115.29.142.212:8020/userCenter.html'

data = {'mobile': '18802094078',
        'password': '45101b093c4e8acf32a525dc231afd50',
        'areaCode': '86'}

headers = {'Accept-Language':'zh-CN,zh'}

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


data2 = {
    'build': '591',
    'floor': '1524',
    'rooms[0][name]': '301',
    'rooms[0][num]': '210',
    'rooms[0][no]': '301',
    'rooms[0][locktype]': '3',
    'rooms[0][layout]': '{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}',
}


if __name__ == "__main__":
    session = requests.session()
    session.cookies = CookieJar()
    hash = hash(login_url)
    print(hash)
    gethash(data, hash)
    print(data['hash'])
    a = session.post(login_api, data=data)
    b = session.get(user_url)
    c = session.post(addroom_url, data=data2, headers =headers)
    print(a.text)
    print(c.text)
