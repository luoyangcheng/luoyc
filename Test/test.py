from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time,os


driver = webdriver.Chrome()
url_path = "http://www.baidu.com"
driver.get(url_path)
time.sleep(5)