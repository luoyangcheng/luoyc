from selenium import webdriver
import time


url = "https://www.baidu.com"
# 使用无头浏览器
# browser = webdriver.FirefoxOptions()
# browser.add_argument('-headless')
# browser = webdriver.Firefox(options=browser)
browser = webdriver.Firefox()
browser.implicitly_wait(3)
browser.get(url)
print('1')
time.sleep(2)
js = 'window.open("https://www.sogou.com");'
browser.execute_script(js)
print('2')
handles = browser.window_handles
browser.switch_to_window(handles[1])
time.sleep(2)
browser.switch_to_window(handles[0])
print(handles)
