import requests
import sys
import io
import time
import hashlib


#改变标准输出的默认编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

#登录时需要POST的数据
data = {'mobile':'18802094078',
        'password':'45101b093c4e8acf32a525dc231afd50',
        'areaCode':'86',
        "hash":"a64eb28672e8b66c105702165ea88646"}

#设置请求头
#headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


#登录时表单提交到的地址（登录接口）
login_url = "http://115.29.142.212:8020/Home/Public/login"

#构造Session
session = requests.Session()

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)
print(resp.text)

#登录后才能访问 或者操作的网页
url = "http://115.29.142.212:8020/Home/Room/addRooms"

#循环添加数据
for i in range(1,2):
     datas = {
         "build":"591",
         "floor":"1443",
         "rooms[0][name]":str(i),
         "rooms[0][num]":str(i),
         "rooms[0][no]": str(i),
         "rooms[0][locktype]": "1",
         "rooms[0][layout]": '{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}'
     }
     r = session.post(url,datas)
     print(r.text)