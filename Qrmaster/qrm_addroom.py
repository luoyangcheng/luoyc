import requests, hashlib
from bs4 import BeautifulSoup

login_url = 'http://192.168.3.19:6112/login.html'
login_api = "http://192.168.3.19:6112/Home/Public/login"
addroom_url = 'http://192.168.3.19:6112/Home/Room/addRooms'

data = {'mobile': '18802094078',
        'password': '45101b093c4e8acf32a525dc231afd50',
        'areaCode': '86'}

headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
           'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
           'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
           'X-Requested-With':'XMLHttpRequest',
           'Accept-Encoding':'gzip, deflate'}

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
    'floor': '1443',
    'rooms[0][name]': '301',
    'rooms[0][num]': '210',
    'rooms[0][no]': '301',
    'rooms[0][locktype]': '3',
    'rooms[0][layout]': '{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}',
}

if __name__ == "__main__":
    session = requests.session()
    hash = hash(login_url)
    print(hash)
    gethash(data, hash)
    print(data['hash'])
    a = session.post(login_api, data=data)
    b = session.post(addroom_url, data=data2, headers =headers)
    print(a.text)
    print(b.text)
