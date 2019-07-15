# 美住登录功能

from selenium import webdriver
from _def import waitid, waittext, read_excel, write_excel
from termcolor import colored


class Login:
    def browser(self):
        excel_path = "D:\git\warehouse\Meizhu\meizhu_testcase.xlsx"
        username = read_excel(excel_path, '美住登录', 1)
        passwd = read_excel(excel_path, '美住登录', 2)
        tip = read_excel(excel_path, '美住登录', 3)
        url = "http://www.meizhuyun.com/login.html"
        # 使用无头浏览器
        # browser = webdriver.FirefoxOptions()
        # browser.add_argument('-headless')
        # browser = webdriver.Firefox(options=browser)
        browser = webdriver.Firefox() # 打开浏览器
        browser.implicitly_wait(3) # 等待3秒
        Result = []
        for x, y, z in zip(username, passwd, tip):
            browser.get(url)
            waitid(browser, "requestUsername")
            browser.find_element_by_id("requestUsername").send_keys(x)
            waitid(browser, "requestPassword")
            browser.find_element_by_id("requestPassword").send_keys(y)
            waitid(browser, "requestSubmit")
            browser.find_element_by_id("requestSubmit").click()
            tip = waittext(browser, "login-tip")
            if tip == z:
                print(colored('测试通过', 'green'))
                result_text = "PASS"
                Result.append(result_text)
            else:
                print(colored('测试失败', 'red'))
                result_text = "FAIL"
                Result.append(result_text)
        write_excel(excel_path, '美住登录', Result) # 把结果写入excel


if __name__ == "__main__":
    Login().browser()
