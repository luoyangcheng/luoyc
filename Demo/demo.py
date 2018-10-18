from selenium import webdriver
import time


url = "https://www.baidu.com"
browser = webdriver.FirefoxOptions()
browser.add_argument('-headless')
browser = webdriver.Firefox(options=browser)
# browser = webdriver.Firefox()
browser.implicitly_wait(3)
browser.get(url)
print('1')
time.sleep(5)
js = 'window.open("https://www.sogou.com");'
browser.execute_script(js)
print('2')
print(browser.current_window_handle)
