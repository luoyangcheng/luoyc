import requests

data = {'mobile': '13480251015', 'vcode': '111111', 'areaCode': '86'}
data2 = {'mobile': '13480251015', 'password': 'qq111111', 'areaCode': '86'}
data3 = {'type': '2'}
sendcode_url = "http://www.meizhuyun.com/Home/Public/checkCode"
editped_url = "http://www.meizhuyun.com/Home/Public/resetPassword"
a = "http://www.meizhuyun.com/Home/Ggboard/getBoard"
resp = requests.post(sendcode_url, data=data)
resp = requests.post(a, data=data3)
resp2 = requests.post(editped_url, data=data2)
print(resp.content.decode('utf-8'))
print(resp2.content.decode('utf-8'))
