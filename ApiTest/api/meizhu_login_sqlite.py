import sys
sys.path.append('../ApiTest/common/')
import Open_Sqlite3, TestRequests


def login(cursor):
    x = TestRequests.Test_Requests()
    expect, actual = [], []
    table_name = 'tb_login'
    maxrow = Open_Sqlite3.max_row(cursor, table_name)
    for i in range(1, maxrow + 1):
        data = Open_Sqlite3.select_data(cursor, table_name, i)
        expect.append(data[3])
        result = x.run_main('login', url='http://www.meizhuyun.com/Home/Public/login', data={'mobile': data[1], 'password': data[2], 'areaCode': data[0]})
        result = result.content.decode('utf-8')
        actual.append(result)
        Open_Sqlite3.update_data(cursor, table_name, i, result)
    return expect, actual
