import sys, json
import pytest
sys.path.append('./')
import api
from api.yyy_api import yyy
from common.Send_Mail import SendMail


class TestVIP(object):
    def setup_class(self):
        print("\n正在开始执行测试用例!")

    def teardown_class(self):
        print("\n所有用例执行完成,开始发送邮件和短信!")
        # Send_Mail.SendMail.mymail(self)
        # Send_SMS.SendSMS()

    @pytest.mark.run(order=1)
    def test_login(self):
        expect, actual = meizhu('login', 'dict', '美住登陆', '/Home/Public/login')
        pytest.assume(expect == actual)

    @pytest.mark.run(order=2)
    def test_addvip(self):
        expect, actual = meizhu('post', 'dict', '添加会员', '/Home/Customer/addVip')
        pytest.assume(expect == actual)

    @pytest.mark.run(order=3)
    def test_viplist(self):
        expect, actual = meizhu('post', 'dict', '会员列表', '/Home/Customer/vip')
        actual = json.loads(actual[0])
        pytest.assume(expect[0] == actual['status'])
        global vipUserId
        vipUserId = actual['data']['item'][0]['id']

    @pytest.mark.run(order=4)
    def test_vipinfo(self):
        expect, actual = meizhu('post', 'dict', '会员详情', '/Home/Customer/setVip', field=['vipUserId'], valu=[vipUserId])
        actual = json.loads(actual[0])
        pytest.assume(expect[0] == actual['status'])


class TestList(object):
    def setup_class(self):
        print("\n正在开始执行测试用例!")

    def teardown_class(self):
        print("\n所有用例执行完成,开始发送邮件和短信!")
        # Send_Mail.SendMail.mymail(self)
        # Send_SMS.SendSMS()

    @pytest.mark.run(order=1)
    def test_searchStreamingOnlineInfo(self):
        expected, result = yyy('post', 'json', 'YOU营养测试用例', 2, 'ip1')
        pytest.assume(expected == result)

    @pytest.mark.run(order=2)
    def test_findStoreDistance(self):
        expected, result = yyy('post', 'json', 'YOU营养测试用例', 3, 'ip2')
        pytest.assume(expected == result)
        
    @pytest.mark.run(order=3)
    def test_getNotificationBar(self):
        expected, result = yyy('post', 'json', 'YOU营养测试用例', 4, 'ip1')
        pytest.assume(expected == result)
        
    @pytest.mark.run(order=4)
    def test_queryProtocolLog(self):
        expected, result = yyy('post', 'json', 'YOU营养测试用例', 5, 'ip2')
        pytest.assume(expected == result)


if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_run.py::TestList", "--html=../yyyTest/report/yyy.html"])
    # pytest --html=report.html,在CMD命令下执行此命令会生成报告
    # pytest -v -s isr_test.py -n 10，多线程运行测试用例，NUM为想要并发的进程数目。
    # python -m pytest ：linux下运行用此方式，因为通过pip安装pytest不会使它成为系统命令，
    # 它会将其安装到python。-m命令将pytest作为自己的命令运行，然后任何进行中的脚本都将成为参数
    # TestClass().test_email() # 此方式可以直接在VScode直接调试某个测试用例模块
    # pip install pytest_assume
    # pip install pytest_html
    # pip install pytest_ordering