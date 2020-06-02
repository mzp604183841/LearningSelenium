from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

myDriver = webdriver.Chrome('/Users/MZP/Desktop/chromedriver')
# 显示等待
wait = WebDriverWait(myDriver, 5, 0.5)
