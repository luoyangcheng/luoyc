import requests
import sys
import io
from meizhu_login import login
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
url = "http://192.168.3.19:8090/Mobile/Hotel/addNoteCost"

#循环添加数据
for i in range(20):
     datas = {
         "userId":"402",
         "token":"mQyjB9S9y36+WrpxAPfk5KbWR2wXdW481MSvEcsFRbuar/RJ9mqdRbH5rL0qpTvc1x5o5Si4uOCBPNRqnd4yycg4NnHIrcZOW2dcOyTFyNudoQecLgitbHSAVa0HQN0Byf1qEULSgm/Ul5s99bJ0y9W/NukeDsf2BLNrOgbJ4Ss21nnIW8sQrPF/XpkoOwOMfwdyvztWaVj2jp4TNLnwhrd09330F+JUiqTW/zX5J96RoqRHPnIhX+whPMdOExMn46ApDHIi4pnMRSiogKE/RRJ0xca1Ipc6/j+ozVavYIEqGZ+4NU0Cjp+MxRdeFPtxdrxu0/gv84ZGtU5XdRUoHQ==",
         "hotel":"309",
         "noteDate":"2018-01-09",
         "noteId": "1826",
         "payId": "900",
         "type": "1",
         "price": "100",
         "remark": "",
     }
     r = session.post(url,datas)
     print(r.content.decode('utf-8'))