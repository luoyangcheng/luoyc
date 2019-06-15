import sys
import os
import pytest
sys.path.append('../TheFame/api/')
import meizhu_login, meizhu_addvip

cur_path = os.path.dirname(os.path.realpath(__file__))
str(cur_path)


def test_login():
    global session  # 设置全局变量
    session = meizhu_login.test_login()


def test_addvip():
    meizhu_addvip.test_addvip(session)


if __name__ == "__main__":
    # pytest --html=report.html,在CMD命令下执行此命令会生成报告
    pytest.main(cur_path + "/test_run.py --html=" + cur_path + "/report/log.html")
