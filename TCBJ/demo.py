import requests
from requests.sessions import session
from tomorrow import threads
import requests, threading


def ll(mobile, password, areaCode):
    data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
    login_url = "https://www.meizhuyun.com/Home/Public/login"
    session = requests.Session()
    session.post(login_url, data)
    return session


@threads(2)
def addroom():
    session = ll(18802094078, 'qq111111', 86)
    data = {'room': '哇哈哈', 'hotel': '371', 'name': '11', 'price': '11', 'charityPrice': '1'}
    addroomurl = 'https://www.meizhuyun.com/Home/Room/addRoom'
    resp = session.post(addroomurl, data)
    print(resp.content.decode('utf-8'))


T = []
for i in range(0, 5):
    t1 = threading.Thread(target=addroom)
    T.append(t1)

if __name__ == '__main__':
    for i in T:
        i.setDaemon(True)
        i.start()
        i.join()