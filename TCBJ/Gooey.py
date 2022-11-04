from locust import HttpUser, TaskSet, task, between, events
import time, json, os, sys, socket
from locust.exception import LocustError
from geventhttpclient import HTTPClient
from geventhttpclient.url import URL


class UserTsak(TaskSet):
    def on_start(self):
        '''初始化数据'''
        url = URL('https://yyj-test.by-health.com')
        self.http = HTTPClient(url.host, url.port, ssl=True, connection_timeout=20, network_timeout=20)

    @task(1)
    def test(self):
        h = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NjY3NjQ4MTksImV4cCI6MTY2Njg1MTIxOSwiaXNzIjoiTWVtYmVyIiwic3ViIjoiMTE0In0.iSwk-c1UetxwL1b7vyV7-Fclvg3ofeTeIbyg2Zpg45jI2pI20VpjKQWXFi2ftI-1GZ8lUoYHCFufnfv5OQLvQQ"}
        r = self.http.post("/scrmv2/liteactivity/221028/queryShareState", headers=h)
        print(r.content.decode('utf-8'))
        print(r.status_code)
        assert r.status_code == 200

    def on_stop(self):
        self.http.close()


class WebsiteUser(HttpUser):
    host = 'https://yyj-test.by-health.com'
    task_set = UserTsak
    wait_time = between(0, 0)
