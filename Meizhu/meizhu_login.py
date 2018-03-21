#
#
# 美住登录功能
from selenium import webdriver
from Meizhu._def import waitid,waitxp
import time
import xlrd


def read_excel():
    data = xlrd.open_workbook('F:\meizhu_testcase.xlsx')
    sheet = data.sheets()[0]
    username = sheet.col_values(0)
    passwd = sheet.col_values(1)
    tip = sheet.col_values(2)
    return username,passwd,tip

def browser():
    username,passwd,tip=read_excel()
    url = "http://192.168.3.19:8090/login.html"
    browser = webdriver.Firefox()
    for x, y, z in zip(username, passwd, tip):
        browser.get(url)
        waitid(browser,"requestUsername")
        browser.find_element_by_id("requestUsername").send_keys(x)
        waitid(browser, "requestPassword")
        browser.find_element_by_id("requestPassword").send_keys(y)
        waitid(browser, "requestSubmit")
        browser.find_element_by_id("requestSubmit").click()
        waitid(browser, "login-tip")
        str = browser.find_element_by_id("login-tip").text
        if str == z:
            print("测试通过")
        else:
            print("\033[1;31m !!!!ERRO!!!! \033[0m!", x, y,str,z)


if __name__ == "__main__":
    browser()