import requests
import sys
import os
sys.path.append('../TheFame/common/')
import logger, excel


def login(mobile, password, areaCode):
    global result, session  # 设置全局变量
    data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
    login_url = "http://www.meizhuyun.com/Home/Public/login"
    session = requests.Session()
    result = session.post(login_url, data)
    result = result.content.decode('utf-8')


def test_login():
    filename = os.path.basename(__file__)  # 获取当前文件名
    log = logger.Log()
    excel_path = "../TheFame/case/case.xlsx"
    mobile = excel.read_excel(excel_path, '美住登陆', 1)
    password = excel.read_excel(excel_path, '美住登陆', 2)
    areaCode = excel.read_excel(excel_path, '美住登陆', 3)
    expected = excel.read_excel(excel_path, '美住登陆', 4)
    actual = []
    for x, y, e, r in zip(mobile, password, areaCode, expected):
        login(x, y, e)
        if result == r:
            log.info(filename + '--' + result)
            actual.append(result)
        else:
            log.error(filename + '--' + result)
            actual.append(result)
    excel.write_excel(excel_path, '美住登陆', actual)
    return session
