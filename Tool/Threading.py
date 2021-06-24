import threading
import requests
import datetime


class login:
    def ll(mobile, password, areaCode):
        data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
        login_url = "https://www.meizhuyun.com/Home/Public/login"
        session = requests.Session()
        print(datetime.datetime.now())
        resp = session.post(login_url, data, verify=False)
        # print(resp.content.decode('utf-8'))
        # print(resp.cookies.get_dict())


T = []
for i in range(10):
    t1 = threading.Thread(target=login.ll, args=('18802094078', 'qq111111', '86'))
    T.append(t1)

if __name__ == '__main__':
    for i in T:
        i.setDaemon(True)
        i.start()
    for j in T:
        j.join()
