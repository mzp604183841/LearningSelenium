from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

myDriver = webdriver.Chrome('/Users/MZP/Desktop/chromedriver')

myDriver.get('http://www.baidu.com')

# 显式等待
wait = WebDriverWait(myDriver, 5, 0.5)

searchFiled = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
searchFiled = wait.until(EC.title_is(())) # 仅用于判断页面的标题是否满足
searchFiled.send_keys('selenium')
time.sleep(3)
myDriver.quit()

# 隐式等待  设置一个定位元素的最长时间，如果小于10秒定位到，程序继续执行，如果超过10秒没有定位到，则抛出异常
# 但是：显式等待和隐式等待 不能一起使用，例如，将隐式等待设置为10秒，将显式等待设置为15秒，可能会导致在20秒后发生超时。

# myDriver.implicitly_wait(10)



