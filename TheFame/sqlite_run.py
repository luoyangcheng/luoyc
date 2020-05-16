import sys
import pytest
import sqlite3
sys.path.append('../TheFame/api/')
import meizhu_login_sqlite, meizhu_addvip_sqlite
sys.path.append('../TheFame/common/')
import Send_Mail, Send_SMS, Open_Sqlite3


class TestVIP(object):
    def setup_class(self):
        print("\n正在打开数据库连接...\n")
        self.conn = sqlite3.connect("../TheFame/case/Meizhu.db")
        self.cursor = self.conn.cursor()

    def teardown_class(self):
        fail_num, tb_name = Open_Sqlite3.statistical_data(self.cursor)
        print("\n失败用例总数：%s" % fail_num)
        print("\n失败用例分布：%s" % tb_name)
        print("\n正在关闭数据库连接...")
        self.conn.commit()
        self.conn.close()
        print("\n正在发送邮件和短信...")
        # Send_Mail.SendMail.mymail(self)
        # Send_SMS.SendSMS()

    @pytest.mark.run(order=1)
    def test_login(self):
        expect, actual = meizhu_login_sqlite.login(self.cursor)
        pytest.assume(expect == actual)

    @pytest.mark.run(order=2)
    def test_addvip(self):
        expect, actual = meizhu_addvip_sqlite.addvip(self.cursor)
        pytest.assume(expect == actual)


if __name__ == "__main__":
    pytest.main(["-s", "sqlite_run.py::TestVIP", "--html=../TheFame/report/Meizhu.html"])
    # pytest --html=report.html,在CMD命令下执行此命令会生成报告
    # pytest -v -s isr_test.py -n 10，多线程运行测试用例，NUM为想要并发的进程数目。
    # python -m pytest ：linux下运行用此方式，因为通过pip安装pytest不会使它成为系统命令，
    # 它会将其安装到python。-m命令将pytest作为自己的命令运行，然后任何进行中的脚本都将成为参数
    # TestClass().test_email() # 此方式可以直接在VScode直接调试某个测试用例模块
    # pip install pytest_assume
    # pip install pytest_html
    # pip install pytest_ordering