import requests
import json


class getroomitem:
    def login(areaCode, account, passwd):
        data1 = {'areaCode': areaCode, 'account': account, 'passwd': passwd}
        login_url = "http://192.168.3.19:6112/mobile/user/login"

        session = requests.Session()
        resp = session.post(login_url, data1)
        r = resp.content.decode('utf-8')
        # print(resp.content.decode('utf-8'))
        f = json.loads(r)
        token = (f["data"]["token"])
        return token

    def room(id, token, communityId, authorityId, enable):
        data2 = {
            'id': id,
            'token': token,
            'communityId': communityId,
            'authorityId': authorityId,
            'enable': enable,
            'type': 5
        }

        header = {'V': '3.0.11'}
        room_url = "http://192.168.3.19:6112/Mobile/power/toggleFunCard"
        resp = requests.post(room_url, data2, headers=header)
        print(resp.content.decode('utf-8'))


if __name__ == '__main__':
    token = getroomitem.login(
        '86', '18802094078',
        'wqP2kdWqnQXr5lHtdC03r5JGwjVzzCYfq9PmW2ZN6idIhdesXQxeIK2+BVQzsmJujuyn7obb/e2mRzsjS+VlRhhC9xyYIMPYe1ilCAt9FKzkdwWfHroHKQgNsw3pWi4FYS/aRUjhYOT+UYEjOnVDZLKhp336qNqTRp7J7Xz3b/4AxZSv/R5otHVwZdluyz9S3IqRAenuiZO73vY/l2z558tOPM9wvcTqBoahuYw+eM3cEslDAmexvAIVjoFL/uSEX1TyAKhMHndx8cxfmhmRI+EOEkRo9nRWQqrcRwrX7SIVkw1UrUX1StwOVEwR5g9bNHwZ8PJi4ZX/qcMlDkrBEQ=='
    )
    # print(token)
    getroomitem.room('2402', token, '537', '52', '1')
