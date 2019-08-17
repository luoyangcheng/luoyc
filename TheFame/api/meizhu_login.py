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
    mobile = Open_Excel.read_excel(excel_path, '美住登陆', 1)
    password = Open_Excel.read_excel(excel_path, '美住登陆', 2)
    areaCode = Open_Excel.read_excel(excel_path, '美住登陆', 3)
    expected = Open_Excel.read_excel(excel_path, '美住登陆', 4)
    actual = []
    for x, y, e, r in zip(mobile, password, areaCode, expected):
        login(x, y, e)
        if result == r:
            log.info(filename + '--' + result)
            actual.append(result)
        else:
            log.error(filename + '--' + result)
            actual.append(result)
    Open_Excel.write_excel(excel_path, '美住登陆', actual)
    return session
