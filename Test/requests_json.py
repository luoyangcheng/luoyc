from Test.meizhu_login import login
import json
from datetime import datetime


class vip:
    def bc(mobile, password, areaCode, hotel, currentPage):
        session = login.ll(mobile, password, areaCode)

        data = {'hotel': hotel, 'currentPage': currentPage}

        login_url = "http://192.168.3.19:8090/Home/Customer/vip"
        startime = datetime.now()
        resp = session.post(login_url, data)
        endtime = datetime.now()
        r = resp.content.decode('utf-8')
        f = json.loads(r)
        vids = []
        for i in range(len(f["data"]["item"])):
            vid = (f["data"]["item"][i]["id"])
            vids.append(vid)
        print(vids)
        print(max(vids))
        print(endtime - startime)


if __name__ == '__main__':
    vip.bc('18802094078', 'qq111111', '86', '309', '1')
