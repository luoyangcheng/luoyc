# encoding=utf-8
import requests
import time

cookies = {
    'master_session_id': 'uhnpv7tqm9tq1f6ooqmvpgod52',
    'qrm_community_identity': '9d4JYo5DvxVpL2lP',
    'qrm_think_language': 'zh_cn'
}
host = "http://qrm.uclbrt.com"
url = "/Home/Room/addRooms"
link = host + url
for i in range(250):
    data = {"build": "1817",
            "floor": "4288",
            "rooms[0][name]": '3_' + str(i),
            "rooms[0][num]": str(i),
            "rooms[0][no]": str(i),
            "rooms[0][locktype]": "1",
            "rooms[0][layout]": '{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}'
            }
    print(data)
    time.sleep(1)
    req = requests.post(link, cookies=cookies, data=data)
    print(req.text)
