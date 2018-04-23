from Test.meizhu_login import login
import json


class vip:
    def bc(mobile, password, areaCode, hotel, currentPage):
        session = login.ll(mobile, password, areaCode)

        data = {'hotel': hotel, 'currentPage': currentPage}

        login_url = "http://192.168.3.19:8090/Home/Customer/vip"
        resp = session.post(login_url, data)
        r = resp.content.decode('utf-8')
        f = json.loads(r)
        vid = []
        for i in range(len(f["data"]["item"])):
            id = (f["data"]["item"][i]["id"])
            vid.append(id)
        print(vid)
        print(max(vid))


if __name__ == '__main__':
    vip.bc('18802094078', 'qq111111', '86', '309', '1')
