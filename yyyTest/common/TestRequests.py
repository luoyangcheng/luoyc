import requests
import sys
sys.path.append('./')
import common
from common.logger import Log


class Test_Requests():
    def get(self, **kwargs):
        '''封装get方法'''
        # 获取请求参数
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        url = kwargs.get('url')
        try:
            result = requests.get(url=url, params=params, headers=headers)
            return result
        except Exception as e:
            print("get请求错误: %s" % e)


    def post(self, url, **kwargs):
        '''封装yyj方法'''
        # 获取请求参数
        log = Log()
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        files = kwargs.get("files")
        headers = kwargs.get("headers")
        try:
            result = requests.post(url, params=params, data=data, json=json, files=files, headers=headers)
            log.info(result.content.decode('utf-8'))
            return result
        except Exception as e:
            print("post请求错误: %s" % e)


    def run_main(self, method, **kwargs):
        '''
        判断请求类型
        :param method: 请求接口类型
        :param kwargs: 填参数
        :return: 接口返回内容
        '''
        if method == 'get':
            result = self.get(**kwargs)
            return result
        elif method == 'post':
            result = self.post(**kwargs)
            return result
        else:
            print('请求接口类型错误')