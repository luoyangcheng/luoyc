from meizhu_login import Meizhu_login
import sys
sys.path.append('E:\luoyc\TheFame\common')
import logger

log = logger.Log()


def test_login():
    # 测试登录，正确账号、正确密码
    log.info("测试登录，正确账号、正确密码")
    session, result = Meizhu_login.login('18802094078', 'qq111111', '86')
    print(result.content.decode('utf-8'))
