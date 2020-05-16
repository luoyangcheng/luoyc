import sys
import pytest
sys.path.append('../ApiTest/api/')
import meizhu_login, meizhu_addvip
sys.path.append('../ApiTest/common/')
import Send_Mail, Send_SMS


def teardown_module(self):
    print("\n所有用例执行完成,开始发送邮件和短信!")
    # Send_Mail.SendMail.mymail(self)
    # Send_SMS.SendSMS()


class TestVIP(object):
    @pytest.mark.run(order=1)
    def test_login(self):
        expect, actual = meizhu_login.login()
        pytest.assume(expect == actual)

    @pytest.mark.run(order=2)
    def test_addvip(self):
        expect, actual = meizhu_addvip.addvip()
        pytest.assume(expect == actual)


class TestOrder(object):
    @pytest.mark.run(order=3)
    def test_demo(self):
        pass


if __name__ == "__main__":
    pytest.main(["-s", "-v", "excel_run.py::TestVIP", "--html=../ApiTest/report/Meizhu.html"])
    # pytest --html=report.html,在CMD命令下执行此命令会生成报告
    # pytest -v -s isr_test.py -n 10，多线程运行测试用例，NUM为想要并发的进程数目。
    # python -m pytest ：linux下运行用此方式，因为通过pip安装pytest不会使它成为系统命令，
    # 它会将其安装到python。-m命令将pytest作为自己的命令运行，然后任何进行中的脚本都将成为参数
    # TestClass().test_email() # 此方式可以直接在VScode直接调试某个测试用例模块
    # pip install pytest_assume
    # pip install pytest_html
    # pip install pytest_ordering