import requests
import json
import time

class getroomitem:
    def login(areaCode, account, passwd):
        data1 = {'areaCode': areaCode,
                 'account': account,
                 'passwd': passwd

                 }
        login_url = "http://115.29.142.212:8020/mobile/user/login"

        session = requests.Session()
        resp = session.post(login_url, data1)
        r = resp.content.decode('utf-8')
        print(resp.content.decode('utf-8'))
        f = json.loads(r)
        token = (f["data"]["token"])
        return token

    def room(communityId, id, token):
        data2 = {'communityId': communityId,
                 'id': id,
                 'token': token}

        header = {'V': '3.0.08'}
        room_url = "http://115.29.142.212:8020/Mobile/Room/item"

        for i in range(10000):
            resp = requests.post(room_url, data2, headers = header)
            print(resp.content.decode('utf-8'))
            time.sleep(1)


if __name__ == '__main__':
    token = getroomitem.login('86', '18802094078',
                              'fCx5Gyw0h98172b+w9StnCDbRxNe+ByEosng3aApcePOkQh7zD37uA9EZfcDwqUksqtl8lnV19ZtZAY7RI9gF06cHY00ObkHxYTJuwPgwWjq1ou/KdsKDUJVj6KkKHIx7vojzhG5M53Iim3kqYqvw8nqBLORebshNknGbrHygX2ff3UnP6Htt0nVfz/b2AQpb6w3a2fmUPzXtw+ikXGkCfBCcMtBZfTnY9EOpRVUAyvdILq3SUuEqYLjdts11cBLNPmCIi4MkQDrmFExq5hEJzcfOpqX4yW+zuhKOOGrvlHtyDXkeZ9XBU4B8onWx4qNOiP1g+pf06Rgr4RftNYQAg==')
    getroomitem.room('819', '4103', token)
