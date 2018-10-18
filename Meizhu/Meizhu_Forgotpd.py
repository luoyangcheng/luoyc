import requests

data = {'mobile': '13480251015', 'vcode': '111111', 'areaCode': '86'}
data2 = {'mobile': '13480251015', 'password': 'qq111111', 'areaCode': '86'}
sendcode_url = "http://192.168.3.19:8090/Home/Public/checkCode"
editped_url = "http://192.168.3.19:8090/Home/Public/resetPassword"
resp = requests.post(sendcode_url, data=data)
resp2 = requests.post(editped_url, data=data2)
print(resp.content.decode('utf-8'))
print(resp2.content.decode('utf-8'))
