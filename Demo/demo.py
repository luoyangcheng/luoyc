import requests
import os

# 禁用警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# help(requests)
url = "https://passport.cnblogs.com/user/signin"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0)Gecko/20100101 Firefox/44.0"}
r = requests.get(url, headers=headers, verify=False)
print(r.status_code)

cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
