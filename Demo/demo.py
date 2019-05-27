from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.uclbrt.qrcloud'
desired_caps['appActivity'] = '.GuideActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3000)

driver.quit()
