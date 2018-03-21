import requests
import sys
import io
from Test.meizhu_login import login
#改变标准输出的默认编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

#登录时需要POST的数据
data = {'mobile':'18802094078',
       'password':'qq111111',
       'areaCode':'86'}

#登录时表单提交到的地址（登录接口）
login_url = "http://192.168.3.19:8090/Home/Public/login"

#构造Session
session = requests.Session()

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)
print(resp.content.decode('utf-8'))

#登录后才能访问 或者操作的网页
url = "http://192.168.3.19:8090/Home/Customer/addVip"

#循环添加数据
for i in range(18802094058,18802094060):
     datas = {
         "hotel":"309",
         "name":"路人甲"+str(i),
         "mobile": str(i),
         "vipInfoId":"465",
         "gender": "0",
         "birthday": "",
         "nation": "",
         "identity": "",
         "address": "",
         "wechat": "",
         "remark": "",
         "share": "1",
         "areaCode": "86",
         "vipLevelName": "黄金"
     }
     r = session.post(url,datas)
     print(r.content.decode('utf-8'))