import requests
import json


class getroomitem:
    def login(areaCode, account, passwd):
        data1 = {'areaCode': areaCode, 'account': account, 'passwd': passwd}
        login_url = "http://192.168.3.19:8082/mobile/user/login"

        session = requests.Session()
        resp = session.post(login_url, data1)
        r = resp.content.decode('utf-8')
        f = json.loads(r)
        token = (f["data"]["token"])
        return token

    def addCustomer(id, token, communityId, areaCode, mobile, name, gender,
                    identify, departname, staffno, staffcardno):
        data2 = {
            'id': id,
            'token': token,
            'communityId': communityId,
            'areaCode': areaCode,
            'mobile': mobile,
            'name': name,
            'gender': gender,
            'identify': identify,
            'departname': departname,
            'staffno': staffno,
            'staffcardno': staffcardno,
        }

        # header = {'V': '3.0.11'}
        room_url = "http://192.168.3.19:8082/mobile/ClientMember/addCustomer"
        resp = requests.post(room_url, data2)
        r = resp.content.decode('utf-8')
        f = json.loads(r)
        customerid = (f["data"]["id"])
        data3 = {
            'id': id,
            'token': token,
            'communityId': communityId,
            'userId': customerid,
            'roomStr': "7269",
            'longOpenRoomStr': "",
        }
        Addpermissions_url = "http://192.168.3.19:8082/mobile/Community/addClientRoomPower2"
        resp2 = requests.post(Addpermissions_url, data3)
        r2 = resp2.content.decode('utf-8')
        print(r2)


if __name__ == '__main__':
    token = getroomitem.login(
        '86', '18802094078',
        'wqP2kdWqnQXr5lHtdC03r5JGwjVzzCYfq9PmW2ZN6idIhdesXQxeIK2+BVQzsmJujuyn7obb/e2mRzsjS+VlRhhC9xyYIMPYe1ilCAt9FKzkdwWfHroHKQgNsw3pWi4FYS/aRUjhYOT+UYEjOnVDZLKhp336qNqTRp7J7Xz3b/4AxZSv/R5otHVwZdluyz9S3IqRAenuiZO73vY/l2z558tOPM9wvcTqBoahuYw+eM3cEslDAmexvAIVjoFL/uSEX1TyAKhMHndx8cxfmhmRI+EOEkRo9nRWQqrcRwrX7SIVkw1UrUX1StwOVEwR5g9bNHwZ8PJi4ZX/qcMlDkrBEQ=='
    )
    print(token)
    for i in range(18802094079, 18802094079):
        getroomitem.addCustomer('2402', token, '723', '86', i, i, '1', '', '',
                                '', '')
