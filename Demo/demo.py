from selenium import webdriver


url = "http://192.168.3.19:8090/login.html"
browser = webdriver.Firefox()
browser.implicitly_wait(3)
browser.get(url)
