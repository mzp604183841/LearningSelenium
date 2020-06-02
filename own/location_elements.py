from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

myDriver = webdriver.Chrome('/Users/MZP/Desktop/chromedriver')
myDriver.get_window_size()
myDriver.get("http://www.baidu.com")

myDriver.find_element_by_id("kw").send_keys('selenium')
myDriver.find_element_by_id('su').click()

# # 获取当前页面的标题
# pageTitle = myDriver.title
#
# # 页面后退
# myDriver.back()
#
# # 页面前进
# myDriver.forward()
#
# # 页面刷新
# myDriver.refresh()

time.sleep(5)

# 当前页面的ID
print(myDriver.current_window_handle) # 打印出来的：CDwindow-197256F6A616A68C66EB9C51F334FB2D

# 尝试打开一个新的标签页
# myDriver.find_element(By.LINK_TEXT, "new window").click() # selenimu 4 才有的API 目前selenium 2好像还没有新建标签页的功能

# 设置等待
wait = WebDriverWait(myDriver, 10)

# myDriver.switch_to_window('tab') # 这也是selenium 4才有的方法，目前不能使用

# 窗口大小相关
width = myDriver.get_window_size().get('wdith')
height = myDriver.get_window_size().get('height')

# 直接设置窗口大小
myDriver.set_window_size()
# 我看到了很多set 设置方法
myDriver.set_network_conditions() # 设置网络模式
myDriver.set_page_load_timeout() # 设置页面加载超时时间
myDriver.set_script_timeout() # 设置页面元素的加载超时时间吧
myDriver.set_window_position() # 设置窗口的左上角的位置
myDriver.set_window_rect() # 设置窗口的起点和长宽
myDriver.maximize_window() # 最大化
myDriver.minimize_window() # 最小化
myDriver.fullscreen_window() # 全屏









myDriver.quit()