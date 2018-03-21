# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Meizhu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3000)
        self.base_url = "http://www.meizhuyun.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_meizhu(self):
        pwd=["111111h","qq111111","aa111111"]
        for x in pwd:
           driver = self.driver
           driver.get(self.base_url + "/login.html")
           driver.find_element_by_id("requestUsername").clear()
           driver.find_element_by_id("requestUsername").send_keys("18802094078")
           driver.find_element_by_id("requestPassword").clear()
           driver.find_element_by_id("requestPassword").send_keys(x)
           driver.find_element_by_id("requestSubmit").click()
           s=driver.find_element_by_id("login-tip").text
           driver.find_element_by_xpath ( ".//*[text()='用户不存在']" )
           if s =='密码不正确':
               print("错误密码:"+x)
               break
           else:
               print("正确密码是："+x)

