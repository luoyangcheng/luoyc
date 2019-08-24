import requests
import json

# 改变标准输出的默认编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 登录时需要POST的数据
data = {'mobile': '18802094078', 'password': 'qq111111', 'areaCode': '86'}

# 登录时表单提交到的地址（登录接口）
login_url = "http://www.meizhuyun.com/Home/Public/login"

# 构造Session
session = requests.Session()

# 在session中发送登录请求，此后这个session里就存储了cookie
# 可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)
print(resp.content.decode('utf-8'))

# 登录后才能访问 或者操作的网页
url = "http://www.meizhuyun.com/Home/Customer/addVip"

# 循环添加数据
file = {'file':('luoyc.jpg', open('D:/meinv.jpg', 'rb'),'imagesss/txt', {})}
data = {'hotel': 277, "config": "default"}
try:
    upload_url = "http://www.meizhuyun.com/Home/File/upload"
    result = session.post(upload_url, data, files = file)
except Exception as e:
    print('接口请求出错！', e)
else:
    result = result.content.decode('utf-8')
    f = json.loads(result)
    head = (f["data"]["filename"])
    data2 = {'name': 'luoyc', 'head': head}
    updateUserInfo_url = "http://www.meizhuyun.com/Home/Account/updateUserInfo"
    result2 = session.post(updateUserInfo_url, data2)
    result2 = result2.content.decode('utf-8')
    print(result2)        

