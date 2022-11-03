from my_fake_useragent import UserAgent
import requests

ua = UserAgent(family='chrome')
res = ua.random()
url = "https://www.baidu.com"
headers = {"User-Agent": res}
response = requests.get(url=url, headers=headers)
print(response.status_code)  # 打印状态码
print(response.request.headers)  # 打印自己的请求头
