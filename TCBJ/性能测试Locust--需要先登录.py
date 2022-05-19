from locust import HttpUser, TaskSet, task


class YYY(TaskSet):
    def zb(self):
        data = {'mobile': 18802094078, 'password': 'qq111111', 'areaCode': 86}
        r = self.client.post("/Home/Public/login", data=data, verify=False)
        # print(r.content.decode('utf-8'))
        # print(r.status_code)
        assert r.status_code == 200

    def on_start(self):
        '''任务开始准备工作：只登录一次'''
        self.zb()

    @task(1)
    def tx(self):
        data = {'room': '哇哈哈', 'hotel': '371', 'name': '11', 'price': '11', 'charityPrice': '1'}
        r = self.client.post("/Home/Room/addRoom", data=data, verify=False)
        # print(r.content.decode('utf-8'))
        # print(r.status_code)
        assert r.status_code == 200


class websitUser(HttpUser):
    tasks = [YYY]
    min_wait = 3000  # 最小等待时间 单位毫秒
    max_wait = 6000  # 最大等待时间 单位毫秒


if __name__ == "__main__":
    import os
    os.system("locust -f ../luoyc/TCBJ/Test.py --host=https://www.meizhuyun.com -t 10")