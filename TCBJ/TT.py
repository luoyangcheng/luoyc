# coding:utf-8
# @task(1)表示权重，值越大，执行的次数占比越大，不写默认是1，0就是不执行

# 报告结果解析：
# Type:请求类型
# Name:请求路径
# Requests:请求数量
# Fails:当前失败请求数量
# Median:中间值，一半服务器响应时间高于该值，一半低于该值
# 90%ile:表示有90%的数据小于此数值
# Average:所有请求的平均响应时间
# Min:请求的最少响应时间
# Max:请求的最大响应时间
# Average size:请求的平均大小
# Current RPS:当前每秒请求数
# Current Failures/s:每秒失败请求

# Total Requests per Second ：每秒请求总数：如果上下波动较大，说明性能不稳定
# Response Time(ms) ：响应时间：黄色为最大时间，绿色为最小时间。一般3-5秒为最佳，超过10秒为较差，最大值如果持续高位就需要进行性能优化
# Number of Users ：虚拟用户数

# 注意事项：
# 1.HttpLocust类从继承 Locust的类，并把它添加一个客户端属性，它是的一个实例 HttpSession，可用于使HTTP请求,这就相当于它自动使用了session机制，类似于client = requests.session()所以后面的请求，直接拿client.get()、client.post()请求就可以了
# 2.如果设置了10个虚拟用户同时启动，并无法做到10个请求同时并发，可能会是 2 / 3个这样并发

import os, json, random
from locust import HttpUser, TaskSet, task


class YYY(TaskSet):
    def beginning(self):
        print("初始化操作")

    def on_start(self):
        '''任务开始准备工作：只登录一次'''
        self.beginning()

    @task(0)
    def zb(self):
        number = str(random.randint(18002094078, 18802994078))
        data = {"phone": number, "loginSource": "flzs", "sourceFrom": "福利助手小程序", "nickName": "Lemon🍋", "headimg": "https://thirdwx.qlogo.cn/mmopen/vi_32/jZFphnk3yRcPOxpC3UNu3ygVBah7pMI7vDoM43dAotZRiaGI8dBMaLrUcYQ1hG31oumLUE90Picd8ianAa00qSFqg/132", "gender": 0}
        res = self.client.post("/scrmv2/auth/wandian/consumer/loginByPhone", json=data, verify=False)
        r = res.content.decode('utf-8')
        f = json.loads(r)
        global authToken, memberId
        authToken = (f["authToken"])
        memberId = (f["memberId"])
        print(authToken)
        assert r.status_code == 200
        # print(r)

    @task(0)
    def tx(self):
        h = {"Authorization": "Bearer " + authToken}
        m = memberId
        data = {"memberId": m, "channelType": 11, "takeSource": "福利助手小程序", "orgId": "1-1MZNP", "orgNo": "66666662"}
        r = self.client.post("/scrmv2/coupons/getCouponsByConditions", json=data, verify=False, headers=h)
        print(r.content.decode('utf-8'))
        print(r.status_code)
        assert r.status_code == 200

    @task(1)
    def queryShareState(self):
        # h = {"Authorization": "Bearer " + authToken}
        h = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NjY3NjQ4MTksImV4cCI6MTY2Njg1MTIxOSwiaXNzIjoiTWVtYmVyIiwic3ViIjoiMTE0In0.iSwk-c1UetxwL1b7vyV7-Fclvg3ofeTeIbyg2Zpg45jI2pI20VpjKQWXFi2ftI-1GZ8lUoYHCFufnfv5OQLvQQ"}
        r = self.client.post("/scrmv2/liteactivity/221028/queryShareState", verify=False, headers=h)
        print(r.content.decode('utf-8'))
        print(r.status_code)
        assert r.status_code == 200


class websitUser(HttpUser):
    tasks = [YYY]
    min_wait = 10  # 最小等待时间 单位毫秒
    max_wait = 60  # 最大等待时间 单位毫秒


if __name__ == "__main__":
    # 【1】不使用分布式时执行：
    # os.system("locust -f ../luoyc/TCBJ/性能测试Locust.py --host=https://yyj-test.by-health.com -t 10")

    # 【2】使用分布式时执行：
    # 查看电脑内核数，电脑搜索【设备管理器】--【处理器】，下面有几条数就算几核
    master0 = os.system("locust -f ../luoyc/TCBJ/性能测试Locust.py --master")  # mater节点只需要执行一次
    worker1 = os.system("locust -f ../luoyc/TCBJ/性能测试Locust.py --worker")  # worker节点根据根据电脑内核数n，就启动n次
