import requests
import urllib
from bs4 import BeautifulSoup

url = 'https://tieba.baidu.com/p/6152244349'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')
course = soup.find_all('img', class_="j_user_sign")
x = 0
path = 'D:/demo/'
for i in course:
    img_URL = i['src']
    urllib.request.urlretrieve(img_URL, path + '%s.jpg' % x)
    print('正在下载：' + img_URL)
