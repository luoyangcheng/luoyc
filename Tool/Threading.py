import threading
import requests
import datetime


class login:
    def ll(mobile, password, areaCode):
        data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
        login_url = "http://192.168.3.19:8090/Home/Public/login"
        session = requests.Session()
        print(datetime.datetime.now())
        resp = session.post(login_url, data)
        print(resp.content.decode('utf-8'))


T = []
for i in range(2):
    t1 = threading.Thread(target=login.ll, args=('18802094078', 'qq111111', '86'))
    T.append(t1)

if __name__ == '__main__':
    for i in T:
        i.setDaemon(True)
        i.start()
    for j in T:
        j.join()
