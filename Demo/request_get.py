import requests

payload = {'key1': 'value', 'key2': 'value2'}
res = requests.get("http://httpbin.org/get", params=payload)
print(res.url)
