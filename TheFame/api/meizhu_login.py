import requests
import sys
import os
sys.path.append('../TheFame/common/')
import logger, Open_Excel


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


def login():
    filename = os.path.basename(__file__)  # 获取当前文件名
    log = logger.Log()
    excel_path = "../TheFame/case/case.xlsx"
    sheet = '美住登陆'
    Open_Excel.update_excel(excel_path, sheet)
    Test_data = []
    for i in range(1, 5):
        one_data = Open_Excel.read_excel(excel_path, sheet, i)
        Test_data.append(one_data)
    actual = []
    for mobile, password, areaCode, expected in zip(Test_data[0], Test_data[1], Test_data[2], Test_data[3]):
        login_api(mobile, password, areaCode)
        if result == expected:
            log.info(filename + '--' + result)
            actual.append(result)
        else:
            log.error(filename + '--' + result)
            actual.append(result)
    Open_Excel.write_excel(excel_path, sheet, actual)
    return session, Test_data[3], actual
