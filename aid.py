import requests
import json

# 改变标准输出的默认编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 登录时需要POST的数据
data = {'account': '演示账号', 'password': 'abcd123456'}

# 登录时表单提交到的地址（登录接口）
login_url = "http://test.demo.aidcloud.cn:8089/rProxy//login/doLogin"

# 构造Session
session = requests.Session()

resp = session.post(login_url, data)
print(resp.content.decode('utf-8'))

file = {'file':('20190523140324_0.csv', open('D:/20190523140324_0.csv', 'r'),'application/vnd.ms-excel', {})}
data = {"name": "大傻子"}
upload_url = "http://test.demo.aidcloud.cn:8089/rProxy//dataPacket/upload"
result = session.post(upload_url, data, files = file)
print(result.content.decode('utf-8'))

res = session.get("http://test.demo.aidcloud.cn:8089/rProxy//menu/menuList")
print(res.content.decode('utf-8'))

    

