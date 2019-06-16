import sys
import os
import pytest
sys.path.append('../TheFame/api/')
import meizhu_login, meizhu_addvip

cur_path = os.path.dirname(os.path.realpath(__file__))
str(cur_path)


class TestClass(object):
    def test_l(self):
        global session  # 设置全局变量
        session = meizhu_login.test_login()

    def test_a(self):
        meizhu_addvip.test_addvip(session)


if __name__ == "__main__":
    # pytest --html=report.html,在CMD命令下执行此命令会生成报告
    # pytest -v -s isr_test.py -n NUM，多线程运行测试用例，NUM为想要并发的进程数目。
    # 教程：https://www.jianshu.com/p/4489b2195a46
    pytest.main()
