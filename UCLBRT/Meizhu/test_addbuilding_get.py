import requests
import json
import unittest
import HTMLTestRunner
import time

class MyTest(unittest.TestCase):  # 封装测试环境的初始化和还原的类
    def setUp(self):  # 放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass

    def tearDown(self):  # 与setUp()相对
        print("end test")
        pass


class test_building_get(MyTest):  # 把这个接口封装一个类，下面的方法是具体的测试用例
    '''''接口名称：添加楼栋'''  # 这个描述接口名称

    def test_building_get(self):
        # 获取登录的token 和用户id
        def login_token_id():
            host = "115.29.142.212:8020"
            link = "/mobile/user/login"
            self.url = "http://" + host + link  # 请求url
            self.data = {  # 请求参数
                'areaCode': '86',
                'account': '13480251015',
                'l': 'zh_cn',
                'passwd': 'J4oXyCwYfNiOD5FlhqL3agZRTP6Futhcsi52Rf+7mYPfo6Lb90xfdEnC/6OBsSqQ5y9b67YzEFPNaaK+p+KgeuNwmkjMkT0Zv61nUbS2YgNUk89DUALv8s0BYS3dnHEwLuy3In2vtOXCYdurgyT0CZWvX+glsKcMochghDAduuaP6dabFWSroPC1ZPuKl6k8YWr+8OVZyTW2NHiUzY9+KFo7NmUAvUagutit6iUzfwONAoA5JNIkb5Lz6mn2TWEriERdJb7pa6TSSsDBik40rw5IB0B+hSZChmlJKBdAwPXwQq2qGFyQQsu80hWvWCkWnx5jGLABqCI4qiHZ0EthLQ==',
            }  # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
            self.r = requests.post(url=self.url, data=self.data)
            if json.loads(self.r.text)['status'] == 200:
                b = (json.loads(self.r.text)['data']['token'], json.loads(self.r.text)['data']['id'])
                return b
        # 获取集群id
        def get_communtity_id(token_with_id):
            host = "115.29.142.212:8020"
            link = "/mobile/Community/getCommunitiesWithAuthority"
            self.url = "http://" + host + link  # 请求url
            self.data = {  # 请求参数
                'id': token_with_id[1],
                'l': 'zh_cn',
                'token': token_with_id[0]
            }  # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
            self.r = requests.post(url=self.url, data=self.data)
            if json.loads(self.r.text)['status'] == 200:
                # print(json.loads(self.r.text)['communities']['communityid'])
                communtity_id = json.loads(self.r.text)['data']['communities'][0]['communityid']
                return communtity_id
        # 获取该用户集群下所有的楼栋的id
        def get_building_id_list(token_with_id, communtity_id):
            host = "115.29.142.212:8020"
            link = "/Mobile/Room/getBFR"
            self.url = "http://" + host + link  # 请求url
            self.data = {  # 请求参数
                'id': token_with_id[1],
                'token': token_with_id[0],
                'communityId': communtity_id
            }
            # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
            self.r = requests.post(url=self.url, data=self.data)
            build_list = []
            if json.loads(self.r.text)['status'] == 200:
                data = json.loads(self.r.text)['data']
                for i in data:
                    build_list.append(i['id'])
            return build_list

        # 获取该用户集群下所有的楼栋的编号num
        def get_building_num(token_with_id, communtity_id, build_id_list):
            host = "115.29.142.212:8020"
            link = "/Mobile/Room/getBuilding"
            self.url = "http://" + host + link  # 请求url
            build_num_list = []
            for i in build_id_list:
                self.data = {  # 请求参数
                    'id': token_with_id[1],
                    'token': token_with_id[0],
                    'communityId': communtity_id,
                    'buildingId': i
                }
                # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
                self.r = requests.post(url=self.url, data=self.data)
                if json.loads(self.r.text)['status'] == 200:
                    build_num = json.loads(self.r.text)['data']['num']
                    build_num_list.append(build_num)
            return build_num_list
        # 获取编号列表中最小的值
        def get_list_min_num(build_num_list):
            temp = build_num_list[0]
            for i in build_num_list:
                if temp > i:
                    temp = i
            return temp
        # 生成一个楼栋编号
        def generate_num(min_num, build_num_list):

            # 查找楼栋编号的最小值
            num = min_num + 1
            if num not in build_num_list:
                return num
            elif num == 255:
                raise '超出范围'
            else:
                return generate_num(num, build_num_list)
        # 添加楼栋
        def addBuilding(build_num, token_with_id, build_id_list):
            host = "115.29.142.212:8020"
            link = "/Mobile/Room/addBuilding"
            self.url = "http://" + host + link  # 请求url
            self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
            # 请求参数
            self.data = {
                'id': token_with_id[1],
                'token': token_with_id[0],
                'name': str(build_num),
                'num': str(build_num),
                'contact': 'www',
                'areaCode': '86',
                'phone': '13480251015',
                'communityId': communtity_id,
                'desc': '',
            }  # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
            r = requests.post(url=self.url, data=self.data, headers=self.headers)
            print("status:" + str(json.loads(r.text)['status']))
            return json.loads(r.text)['status']

        token_with_id = login_token_id()
        communtity_id = get_communtity_id(token_with_id)
        build_id_list = get_building_id_list(token_with_id, communtity_id)

        build_num_list = get_building_num(token_with_id, communtity_id, build_id_list)
        build_num_list = [int(i) for i in build_num_list]

        min_num = get_list_min_num(build_num_list)
        build_num = generate_num(min_num, build_num_list)
        status = addBuilding(build_num, token_with_id, build_id_list)
        self.assertEqual(200, status, '添加失败')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(test_building_get('test_building_get'))
    now=time.strftime("%Y%m%d",time.localtime(time.time()))
    # runner = unittest.TextTestRunner()
    fr = open(now+'_addBuilding.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr, title='测试报告', description='测试报告详情')
    runner.run(suite)
