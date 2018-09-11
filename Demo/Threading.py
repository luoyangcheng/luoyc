import threading
import requests
import datetime


class login:
    def ll(mobile, password, areaCode):
        for i in range(5):
            data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
            login_url = "http://192.168.3.19:8090/Home/Public/login"
            session = requests.Session()
            print(datetime.datetime.now())
            resp = session.post(login_url, data)
            print(resp.content.decode('utf-8'))


if __name__ == '__main__':
    t1 = threading.Thread(target=login.ll, args=('17094101202', '111111b', '86'))
    t2 = threading.Thread(target=login.ll, args=('18802094078', 'qq111111', '86'))
    t3 = threading.Thread(target=login.ll, args=('13480251015', '111111b', '86'))
    t1.setDaemon(False)
    t2.setDaemon(False)
    t3.setDaemon(False)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
