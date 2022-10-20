# coding:utf-8
# @task(1)表示权重，值越大，执行的次数占比越大

# 报告结果解析：
# Type:请求类型
# Name:请求路径
# Requests:请求数量
# Fails:当前失败请求数量
# Median:中间值，一半服务器响应时间高于该值，一半低于该值
# 90%ile:90%服务器响应时间
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

from locust import HttpUser, TaskSet, task
import time


class YYY(TaskSet):
    @task(1)
    def zb(self):
        shijian = int(time.time() * 1000)
        data = {"guid": "1721C5D2-17F0-440A-9DBD-5BFC76A0CBE4", "reqId": shijian, "jsonInfo": {"actType": "LOTTERY", "orderId": 2581057, "memberId": 20, "createTime": shijian, "uploadTime": "2022-08-25T06:34:01.990Z", "mobilePhone": "13246492686", "totalPoints": 1000, "presentLegalLevel": 0}}
        r = self.client.post("/services/v1/upload", json=data, verify=False)
        print(r.content.decode('utf-8'))
        print(r.status_code)
        assert r.status_code == 200


class websitUser(HttpUser):
    tasks = [YYY]
    min_wait = 3000  # 最小等待时间 单位毫秒
    max_wait = 6000  # 最大等待时间 单位毫秒


if __name__ == "__main__":
    import os
    os.system("locust -f ../luoyc/TCBJ/性能测试Locust.py --host=http://172.16.8.88:6581 -t 10")