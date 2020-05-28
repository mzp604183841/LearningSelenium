from selenium import webdriver
import time

myDriver = webdriver.Chrome('/Users/MZP/Desktop/chromedriver')
myDriver.get_window_size()
myDriver.get("http://www.baidu.com")

myDriver.find_element_by_id("kw").send_keys('selenium')
myDriver.find_element_by_id('su').click()

pageTitle = myDriver.title
print('页面标题: ' + pageTitle)
time.sleep(2)
myDriver.back()
time.sleep(2)
myDriver.forward()
time.sleep(2)

myDriver.quit()