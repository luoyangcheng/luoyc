from selenium import webdriver
from _def import wait_id, wait_id_text, read_excel, write_excel,wait_name,wait_css,wait_classname
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
        wait_name(browser, "username")
        browser.find_element_by_name("username").send_keys("luoyc")
        wait_id(browser, "password")
        browser.find_element_by_id("password").send_keys("qq111111")
        wait_name(browser, "rememberMe")
        browser.find_element_by_name("rememberMe").click()
        wait_css(browser, "button")
        browser.find_element_by_css_selector("button").click()
        wait_classname(browser, "item")
        browser.find_elements_by_class_name("item")[2].click()


if __name__ == "__main__":
    Login().browser()
