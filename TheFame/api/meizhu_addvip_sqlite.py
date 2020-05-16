import sys
import os
sys.path.append('../TheFame/common/')
import Open_Sqlite3


def addvip_api(session, hotel, name, mobile, vipInfoId, gender, share, areaCode, vipLevelName):
    global result  # 设置全局变量
    data = {'hotel': hotel, 'name': name, 'mobile': mobile, "vipInfoId": vipInfoId, "gender": gender, "share": share, "areaCode": areaCode, "vipLevelName": vipLevelName}
    try:
        addvip_url = "http://www.meizhuyun.com/Home/Customer/addVip"
        result = session.post(addvip_url, data)
    except Exception as e:
        print('接口请求出错！', e)
    else:
        result = result.content.decode('utf-8')


def addvip(session, cursor):
    expect, actual = [], []
    table_name = 'tb_addvip'
    maxrow = Open_Sqlite3.max_row(cursor, table_name)
    for i in range(1, maxrow + 1):
        data = Open_Sqlite3.select_data(cursor ,table_name, i)
        expect.append(data[8])
        addvip_api(session, data[0], data[1], data[3], data[4], data[5], data[6], data[2], data[7])
        actual.append(result)
        Open_Sqlite3.update_data(cursor, table_name, i, result)
    return expect, actual
