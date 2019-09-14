import requests
import urllib3

urllib3.disable_warnings() # 忽略警告
res = requests.get("https://github.com", verify=False)
print(res.status_code)