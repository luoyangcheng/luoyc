# 显性等待时间公共函数
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def waitxp(browser, xpath):
    locator = (By.XPATH, xpath)
    try:
        WebDriverWait(browser, 5, 0.5).until(
            EC.visibility_of_element_located(locator))
    except Exception as e:
        print(e)


def waitid(browser, id):
    locator = (By.ID, id)
    try:
        WebDriverWait(browser, 5, 0.5).until(
            EC.visibility_of_element_located(locator))
    except Exception as e:
        print(e)


def waittext(browser, id):
    locator = (By.ID, id)
    try:
        WebDriverWait(browser, 5, 0.5).until(
            EC.visibility_of_element_located(locator))
        return browser.find_element_by_id(id).text
    except Exception as e:
        return ""
