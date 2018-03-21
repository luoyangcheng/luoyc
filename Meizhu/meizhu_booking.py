#
#提交订单-间夜房
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Meizhu._def import waitid,waitxp
import time
import xlrd

# def read_excel():
#     data = xlrd.open_workbook('F:\meizhu_testcase.xlsx')
#     sheet = data.sheets()[0]
#     username = sheet.col_values(0)
#     passwd = sheet.col_values(1)
#     tip = sheet.col_values(2)
#     return username,passwd,tip


def login(browser):
    # username,passwd,tip=read_excel()
    url = "http://192.168.3.19:8090/login.html"
    browser.get(url)
    browser.find_element_by_id("requestUsername").send_keys("18802094078")
    browser.find_element_by_id("requestPassword").send_keys("qq111111")
    browser.find_element_by_id("requestSubmit").click()

def booking(browser):
    waitxp(browser,'//*[@id="orderListBody"]/tr[1]/td[4]/div')
    browser.find_element_by_xpath('//*[@id="orderListBody"]/tr[1]/td[4]/div').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="addOrderRoom"]/table/tbody/tr[2]/td[1]/input').send_keys("自动化")
    browser.find_element_by_xpath('//*[@id="addOrderRoom"]/table/tbody/tr[2]/td[2]/div[2]/input').send_keys("15802094078")
    browser.find_element_by_xpath('//*[@id="addOrderRoom"]/table/tbody/tr[2]/td[3]/input').send_keys("")
    browser.find_element_by_xpath('//*[@id="addOrderReceive"]/tbody/tr/td[4]/div/input').send_keys("100")
    waitid(browser,"addReceipt")
    browser.find_element_by_id("addReceipt").click()
    waitxp(browser,'//*[@id="addOrderReceive"]/tbody/tr[2]/td[1]/div/a')
    browser.find_element_by_xpath('//*[@id="addOrderReceive"]/tbody/tr[2]/td[1]/div/a').click()
    waitxp(browser,'//*[@id="addOrderReceive"]/tbody/tr[2]/td[1]/div/ul/li[2]/a')
    browser.find_element_by_xpath('//*[@id="addOrderReceive"]/tbody/tr[2]/td[1]/div/ul/li[2]/a').click()
    browser.find_element_by_xpath('//*[@id="addOrderReceive"]/tbody/tr[2]/td[4]/div/input').send_keys("50")
    browser.find_element_by_id("submitBook").click()

    waitid(browser,"initCheckIn")
    browser.find_element_by_id("initCheckIn").click()
    waitid(browser, "checkInConfirm")
    browser.find_element_by_id("checkInConfirm").click()
    waitid(browser, "confirmEnterBtnL")
    browser.find_element_by_id("confirmEnterBtnL").click()


if __name__ == "__main__":
    browser = webdriver.Firefox()
    login(browser)
    booking(browser)
