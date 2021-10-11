import sys
sys.path.append('../ApiTest/common/')
import Open_Sqlite3, TestRequests


def addvip(cursor):
    x = TestRequests.Test_Requests()
    expect, actual = [], []
    table_name = 'tb_addvip'
    maxrow = Open_Sqlite3.max_row(cursor, table_name)
    for i in range(1, maxrow + 1):
        data = Open_Sqlite3.select_data(cursor, table_name, i)
        expect.append(data[8])
        result = x.run_main('post', url='http://www.meizhuyun.com/Home/Customer/addVip', data={'hotel': data[0], 'name': data[1], 'mobile': data[3], 'vipInfoId': data[4], 'gender': data[5], 'share': data[6], 'areaCode': data[2], 'vipLevelName': data[7]})
        result = result.content.decode('utf-8')
        actual.append(result)
        Open_Sqlite3.update_data(cursor, table_name, i, result)
    return expect, actual
