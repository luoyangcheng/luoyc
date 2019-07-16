# 美住登录功能

from selenium import webdriver
from _def import waitid, waittext, read_excel, write_excel,waitname,waitcss,waitclassname
from termcolor import colored


class Login:
    def browser(self):
        url = "http://192.168.100.108/cas/login.aspx"
        # 使用无头浏览器
        # browser = webdriver.FirefoxOptions()
        # browser.add_argument('-headless')
        # browser = webdriver.Firefox(options=browser)
        browser = webdriver.Firefox() # 打开浏览器
        browser.implicitly_wait(3) # 等待3秒
        browser.get(url)
        waitname(browser, "username")
        browser.find_element_by_name("username").send_keys("luoyc")
        waitid(browser, "password")
        browser.find_element_by_id("password").send_keys("qq111111")
        waitname(browser, "rememberMe")
        browser.find_element_by_name("rememberMe").click()
        waitcss(browser, "button")
        browser.find_element_by_css_selector("button").click()
        waitclassname(browser, "img3")
        browser.find_element_by_class_name("img3").click()


if __name__ == "__main__":
    Login().browser()
