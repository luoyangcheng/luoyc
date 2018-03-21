#显性等待时间公共函数
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import time

def waitxp(b,xpath):
    locator = (By.XPATH, xpath)
    try:
        WebDriverWait(b, 20, 0.5).until(EC.visibility_of_element_located(locator))
    finally:
        pass

def waitid(b,id):
    locator = (By.ID, id)
    try:
        WebDriverWait(b, 20, 0.5).until(EC.visibility_of_element_located(locator))
        time.sleep(2)
    except TimeoutException as msg:
        pass
    except NoSuchElementException as msg:
        pass
