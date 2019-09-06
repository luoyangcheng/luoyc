import requests
import json
import time


class getroomitem:
    def login(areaCode, account, passwd):
        data1 = {'areaCode': areaCode,
                 'account': account,
                 'passwd': passwd

                 }
        login_url = "http://192.168.3.19:6112/mobile/user/login"

        session = requests.Session()
        resp = session.post(login_url, data1)
        r = resp.content.decode('utf-8')
        print(resp.content.decode('utf-8'))
        f = json.loads(r)
        token = (f["data"]["token"])
        return token

    def room(id, token, communityId, buildingId, floorId, rooms):
        data2 = {'id': id,
                 'token': token,
                 'communityId': communityId,
                 'buildingId': buildingId,
                 'floorId': floorId,
                 'rooms': rooms}

        header = {'V': '3.0.08'}
        room_url = "http://192.168.3.19:6112/Mobile/Room/addRooms"
        resp = requests.post(room_url, data2, headers=header)
        print(resp.content.decode('utf-8'))
        # time.sleep(1)


if __name__ == '__main__':
    token = getroomitem.login('86', '18802094078',
                              'fCx5Gyw0h98172b+w9StnCDbRxNe+ByEosng3aApcePOkQh7zD37uA9EZfcDwqUksqtl8lnV19ZtZAY7RI9gF06cHY00ObkHxYTJuwPgwWjq1ou/KdsKDUJVj6KkKHIx7vojzhG5M53Iim3kqYqvw8nqBLORebshNknGbrHygX2ff3UnP6Htt0nVfz/b2AQpb6w3a2fmUPzXtw+ikXGkCfBCcMtBZfTnY9EOpRVUAyvdILq3SUuEqYLjdts11cBLNPmCIi4MkQDrmFExq5hEJzcfOpqX4yW+zuhKOOGrvlHtyDXkeZ9XBU4B8onWx4qNOiP1g+pf06Rgr4RftNYQAg==')
    for i in range(255):
        data = {
            "locktype": '6',
            "name": '4'+str(i),
            "no": str(i),
            "num": str(i)
        }
        a = json.dumps(data)
        rooms = '[' + a + ']'
        getroomitem.room('2402', token, '559', '609', '1630', rooms)

