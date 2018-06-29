import requests

data = {'hotel': '277', 'price': '0.01'}
getAccountBank_url = "http://115.29.142.212:8010/Home/Withdraw/getAccountBank"
resp = requests.post(getAccountBank_url, data=data)
print(resp.content.decode('utf-8'))
