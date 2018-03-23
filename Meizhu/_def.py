#显性等待时间公共函数
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#通过xpath的显性等待方法
def waitxp(b,xpath):
    locator = (By.XPATH, xpath)
    try:
        WebDriverWait(b, 20, 0.5).until(EC.visibility_of_element_located(locator))
    except IOError:
        print('仍然找不到元素')
        return None

#通过id的显性等待方法
def waitid(b,id):
    locator = (By.ID, id)
    try:
        WebDriverWait(b, 20, 0.5).until(EC.visibility_of_element_located(locator))
    except IOError:
        print('仍然找不到元素')
        return None
    # except TimeoutException as msg:
    #     pass
    # except NoSuchElementException as msg:
    #     pass

def waitclass(b,classname):
    locator = (By.CLASS_NAME, classname)
    try:
        WebDriverWait(b, 20, 0.5).until(EC.visibility_of_element_located(locator))
    except IOError:
        print('仍然找不到元素')
        return None

def waitname(b,name):
    locator = (By.NAME, name)
    try:
        WebDriverWait(b, 20, 0.5).until(EC.visibility_of_element_located(locator))
    except IOError:
        print('仍然找不到元素')
        return None

def waitline(b,line):
    locator = (By.LINK_TEXT, line)
    try:
        WebDriverWait(b, 20, 0.5).until(EC.visibility_of_element_located(locator))
    except IOError:
        print('仍然找不到元素')
        return None
