import requests
import sys
import os
sys.path.append('../TheFame/common/')
import logger, Open_Excel


def login(mobile, password, areaCode):
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


def test_login():
    filename = os.path.basename(__file__)  # 获取当前文件名
    log = logger.Log()
    excel_path = "../TheFame/case/case.xlsx"
    for i range(1, 4):
        Test_data = []
        one_data = Open_Excel.read_excel(excel_path, '美住登陆', i)
        Test_data.append(one_data)
    actual = []
    for mobile, password, areaCode, expected in zip(Test_data[0], Test_data[1], Test_data[2], Test_data[3]):
        login(mobile, password, areaCode)
        if result == expected:
            log.info(filename + '--' + result)
            actual.append(result)
        else:
            log.error(filename + '--' + result)
            actual.append(result)
    Open_Excel.write_excel(excel_path, '美住登陆', actual)
    return session
