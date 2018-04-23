import requests, hashlib
from bs4 import BeautifulSoup

url = 'http://192.168.3.19:8082/login.html'


def md5(str):
    m = hashlib.md5(str.encode("utf-8"))
    return m.hexdigest()


soup = BeautifulSoup(requests.get(url).text, 'html.parser')
course = soup.find_all('div', class_="card")
for i in course:
    hash = i['data-hash']
    hashtext = md5(hash)
print(hash)
print(hashtext)
