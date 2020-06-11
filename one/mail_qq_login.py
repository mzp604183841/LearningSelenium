from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

myDriver = webdriver.Chrome('/Users/MZP/Desktop/chromedriver')
myDriver.get("http://mail.qq.com")

# 设置显式等待
wait = WebDriverWait(myDriver, 3, 0.5)

# 利用显式等待，定位到登录frame
login_frame = wait.until(EC.presence_of_element_located((By.ID, "login_frame")))
# login_frame = wait.until(myDriver.find_element_by_id('login_frame'))

# 拿到登录frame之后，切换过去，很明显已经不推荐使用的方法了
myDriver.switch_to_frame(login_frame)

# 定位用户名和密码
myDriver.find_element_by_class_name('inputstyle').clear()
time.sleep(1)
myDriver.find_element_by_class_name('inputstyle').send_keys('604183841')
# time.sleep(1)
# myDriver.find_element_by_class_name('inputstyle password').clear()
# time.sleep(1)
# myDriver.find_element_by_class_name('inputstyle password').send_keys('NEWLIFE1992')
time.sleep(1)

# 定位登录按钮
myDriver.find_element_by_id('login_button').click()
time.sleep(1)

myDriver.quit()


