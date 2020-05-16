import requests
import sys
import os
sys.path.append('../TheFame/common/')
import Open_Sqlite3

def login_api(mobile, password, areaCode):
    global result, session  # 设置全局变量
    data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
    try:
        login_url = "http://www.meizhuyun.com/Home/Public/login"
        session = requests.Session()
        result = session.post(login_url, data)
    except Exception as e:
        print('接口请求出错！', e)
    else:
        result = result.content.decode('utf-8')


def login(cursor):
    expect, actual = [], []
    table_name = 'tb_login'
    maxrow = Open_Sqlite3.max_row(cursor, table_name)
    for i in range(1, maxrow + 1):
        data = Open_Sqlite3.select_data(cursor ,table_name, i)
        expect.append(data[3])
        login_api(data[1], data[2], data[0])
        actual.append(result)
        Open_Sqlite3.update_data(cursor, table_name, i, result)
    return session, expect, actual
