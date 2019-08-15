import sys
import os
import pytest
sys.path.append('../TheFame/api/')
import meizhu_login, meizhu_addvip
sys.path.append('../TheFame/common/')
import Send_mail

cur_path = os.path.dirname(os.path.realpath(__file__))
str(cur_path)


class TestClass(object):
    def test_l(self):
        global session  # 设置全局变量
        session = meizhu_login.test_login()

    def test_a(self):
        meizhu_addvip.test_addvip(session)
		
    # 需要发送邮件是打开
    # def test_email(self):
        # Send_mail.SendMail.mymail(self)

if __name__ == "__main__":
    # pytest --html=report.html,在CMD命令下执行此命令会生成报告
    # pytest -v -s isr_test.py -n NUM，多线程运行测试用例，NUM为想要并发的进程数目。
	# python -m pytest ：linux下运行用此方式，因为通过pip安装pytest不会使它成为系统命令，它会将其安装到python。-m命令将pytest作为自己的命令运行，然后任何进行中的脚本都将成为参数
    # 教程：https://www.jianshu.com/p/4489b2195a46
    pytest.main()
