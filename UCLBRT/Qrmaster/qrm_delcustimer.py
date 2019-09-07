import pymysql
import requests
import json


class DATA2():
    try:

        def __init__(self):
            # 连接数据库
            config = {
                'host': '192.168.3.19',
                'port': 3306,
                'user': 'root',
                'passwd': 'hongwei',
                'charset': 'utf8mb4',
                'db': 'qrclient',
                'cursorclass': pymysql.cursors.DictCursor
            }
            self.conn = pymysql.connect(**config)
            self.conn.autocommit(1)
            self.cursor = self.conn.cursor()

        # 查询数据条目
        def SELECT(self, phone):
            TABLE_NAME = 'tb_user_login'
            FIELD_NAME = 'mobile'
            STR_NAME = phone
            FIELD_NAME2 = 'areacode'
            self.count = self.cursor.execute(
                'SELECT * FROM %s WHERE %s = %s AND  %s = 86' %
                (TABLE_NAME, FIELD_NAME, STR_NAME, FIELD_NAME2))
            # 显示所有结果
            cds = self.cursor.fetchall()
            self.cursor.close()
            self.conn.close()
            total = self.cursor.rowcount
            if total != 0:
                f = cds[0]
                id = (f["id"])
                return id
            else:
                print(str(phone) + "没有找到此账号")
                return 0

        def login(self, areaCode, account, passwd):
            data1 = {
                'areaCode': areaCode,
                'account': account,
                'passwd': passwd
            }
            login_url = "http://192.168.3.19:8082/mobile/user/login"
            session = requests.Session()
            resp = session.post(login_url, data1)
            r = resp.content.decode('utf-8')
            f = json.loads(r)
            token = (f["data"]["token"])
            return token

        def delCustomer(self, id, token, communityId, phone):
            customerid = DATA2().SELECT(phone)
            if customerid != 0:
                data = {
                    'id': id,
                    'token': token,
                    'communityId': communityId,
                    'userId': customerid,
                    'roomStr': "",
                    'longOpenRoomStr': "",
                }
                Addpermissions_url = "http://192.168.3.19:8082/mobile/Community/addClientRoomPower2"
                resp = requests.post(Addpermissions_url, data)
                r = resp.content.decode('utf-8')
                print(str(phone) + ':' + r)
            else:
                print(str(phone) + ":修改权限失败")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    token = DATA2().login(
        '86', '18802094078',
        'wqP2kdWqnQXr5lHtdC03r5JGwjVzzCYfq9PmW2ZN6idIhdesXQxeIK2+BVQzsmJujuyn7obb/e2mRzsjS+VlRhhC9xyYIMPYe1ilCAt9FKzkdwWfHroHKQgNsw3pWi4FYS/aRUjhYOT+UYEjOnVDZLKhp336qNqTRp7J7Xz3b/4AxZSv/R5otHVwZdluyz9S3IqRAenuiZO73vY/l2z558tOPM9wvcTqBoahuYw+eM3cEslDAmexvAIVjoFL/uSEX1TyAKhMHndx8cxfmhmRI+EOEkRo9nRWQqrcRwrX7SIVkw1UrUX1StwOVEwR5g9bNHwZ8PJi4ZX/qcMlDkrBEQ=='
    )
    for i in range(18802094078, 18802094179):
        DATA2().delCustomer('2402', token, '723', i)
