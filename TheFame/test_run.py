import sys
import os
import pytest
sys.path.append('../TheFame/case/')
import meizhu_login, meizhu_addvip


def test_login():
    global session  # 设置全局变量
    session = meizhu_login.test_login()


def test_addvip():
    meizhu_addvip.test_addvip(session)


if __name__ == "__main__":
    cur_path = os.path.dirname(os.path.realpath(__file__))
    pytest.main(
        str(cur_path) + "\\test_run.py --html=" + str(cur_path) +
        "\\report\log.html")
