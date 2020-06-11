import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


myDriver = webdriver.Chrome('/Users/MZP/Desktop/chromedriver')
myDriver.get('https://www.126.com')
myDriver.implicitly_wait(1)

# myDriver.find_element_by_id("idInput").clear()
# myDriver.find_element_by_xpath('//input[@id="auto-id-1591854194248"]').send_keys('maozhipeng1992')
# myDriver.find_element_by_xpath('/html/body/div[1]/div[2]/a[1]').click()

# myDriver.find_element_by_class_name('new-loginFuncApp qrcode-126-icon').click()
# myDriver.find_element_by_xpath('//*[@id="lbApp"]').click()

# 切换 frame/iframe 才能定位到一些元素，比如这个例子，在实际过程中，注意网页中的 frame标签

# myDriver.switch_to_frame('x-URS-iframe1591855174467.065')
# myDriver.find_element_by_id("idInput").clear()
# myDriver.find_element_by_xpath('//input[@id="auto-id-1591854194248"]').send_keys('maozhipeng1992')
# 126邮箱的这个iframe 每次都是随机生成的，厉害了我的哥，这个要怎么整

searchField = myDriver.find_element_by_class_name('loginUrs')
myDriver.switch_to_frame(searchField)
time.sleep(2)
myDriver.find_element_by_id("idInput").clear()
text = myDriver.find_element_by_id("idInput").text
print(text)
myDriver.find_element_by_xpath('//input[@id="auto-id-1591854194248"]').send_keys('maozhipeng1992')

time.sleep(3)

myDriver.quit()


