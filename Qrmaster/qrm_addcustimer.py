import requests
import json
import threading


class getroomitem:
    def login(areaCode, account, passwd):
        data1 = {'areaCode': areaCode, 'account': account, 'passwd': passwd}
        login_url = "http://115.29.142.212:8320/mobile/user/login"

        session = requests.Session()
        resp = session.post(login_url, data1)
        r = resp.content.decode('utf-8')
        f = json.loads(r)
        token = (f["data"]["token"])
        return token

    def addCustomer(id, token, communityId, areaCode, starmobile, endmobile,
                    gender, identify, departname, staffno, staffcardno):
        for i in range(starmobile, endmobile):
            data2 = {
                'id': id,
                'token': token,
                'communityId': communityId,
                'areaCode': areaCode,
                'mobile': str(i),
                'name': str(i),
                'gender': gender,
                'identify': identify,
                'departname': departname,
                'staffno': staffno,
                'staffcardno': staffcardno,
            }
            room_url = "http://115.29.142.212:8320/mobile/ClientMember/addCustomer"
            resp = requests.post(room_url, data2)
            code = resp.status_code
            if code == 200:
                r = resp.content.decode('utf-8')
                f = json.loads(r)
                customerid = (f["data"]["id"])
                data3 = {
                    'id': id,
                    'token': token,
                    'communityId': communityId,
                    'userId': customerid,
                    'roomStr': "18831",
                    'longOpenRoomStr': "",
                }
                Addpermissions_url = "http://115.29.142.212:8320/mobile/Community/addClientRoomPower2"
                resp2 = requests.post(Addpermissions_url, data3)
                r2 = resp2.content.decode('utf-8')
                print(r2)
            else:
                print("手机号已存在")


token = getroomitem.login(
    '86', '18802094078',
    'wqP2kdWqnQXr5lHtdC03r5JGwjVzzCYfq9PmW2ZN6idIhdesXQxeIK2+BVQzsmJujuyn7obb/e2mRzsjS+VlRhhC9xyYIMPYe1ilCAt9FKzkdwWfHroHKQgNsw3pWi4FYS/aRUjhYOT+UYEjOnVDZLKhp336qNqTRp7J7Xz3b/4AxZSv/R5otHVwZdluyz9S3IqRAenuiZO73vY/l2z558tOPM9wvcTqBoahuYw+eM3cEslDAmexvAIVjoFL/uSEX1TyAKhMHndx8cxfmhmRI+EOEkRo9nRWQqrcRwrX7SIVkw1UrUX1StwOVEwR5g9bNHwZ8PJi4ZX/qcMlDkrBEQ=='
)
t1 = threading.Thread(
    target=getroomitem.addCustomer,
    args=('4103', token, '2211', '86', 18802094413, 18802095078, '1', '', '',
          '', ''))

if __name__ == '__main__':
    t1.setDaemon(True)
    t1.start()
    t1.join()
