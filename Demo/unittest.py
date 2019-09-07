from Test.unittest_def import sub, sum
import unittest


class mytest(unittest.TestCase):
    ## 初始化工作
    def setUp(self):
        pass

    # 退出清理工作
    def tearDown(self):
        pass

    # 具体的测试用例，一定要以test开头
    def testsum(self):
        self.assertEqual(sum(1, 2), 3, 'test sum fail')

    def testsub(self):
        self.assertEqual(sub(2, 1), 1, 'test sub fail')


if __name__ == '__main__':
    unittest.main()
