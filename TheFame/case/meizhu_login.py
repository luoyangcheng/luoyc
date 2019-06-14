import requests
import sys
import os
sys.path.append('../TheFame/common/')
import logger


def login(mobile, password, areaCode):
    global result, session  # 设置全局变量
    data = {'mobile': mobile, 'password': password, 'areaCode': areaCode}
    login_url = "http://www.meizhuyun.com/Home/Public/login"
    session = requests.Session()
    result = session.post(login_url, data)
    result = result.content.decode('utf-8')


def test_login():
    # 测试登录，正确账号、正确密码
    login('18802094078', 'qq111111', '86')
    filename = os.path.basename(__file__)
    log = logger.Log()
    log.info(filename + result)
    return session
