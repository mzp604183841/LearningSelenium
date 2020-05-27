from selenium import webdriver
import time


myDriver = webdriver.Chrome('/Users/MZP/Desktop/chromedriver')
myDriver.get_window_size()
myDriver.get("http://www.baidu.com")


