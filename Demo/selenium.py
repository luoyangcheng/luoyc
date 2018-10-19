from selenium import webdriver
import time


url = "https://www.baidu.com"
# 使用无头浏览器
# browser = webdriver.FirefoxOptions()
# browser.add_argument('-headless')
# browser = webdriver.Firefox(options=browser)
browser = webdriver.Firefox()
browser.implicitly_wait(3)
browser.get('http://www.baidu.com')

# 获取当前窗口的句柄
currentWin = browser.current_window_handle

# 跳转到另一个新页面
browser.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
# 获取所有窗口的句柄
handles = browser.window_handles
for i in handles:
    if currentWin == i:
        continue
    else:
        # 将driver与新的页面绑定起来
        browser = browser.switch_to_window(i)
# 在新的页面定位元素
# browser.find_element_by_xpath("//*[@id='u1']/a[1]").click()
time.sleep(2)
browser.quit()
# browser.switch_to_window(handles[1])
# browser.switch_to_window(handles[0])
print(handles)
print(currentWin)
