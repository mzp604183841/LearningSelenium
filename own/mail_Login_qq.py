from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
myDriver = webdriver.Chrome("/Users/MZP/Desktop/chromedriver")
myDriver.get("http://mail.qq.com")

wait = WebDriverWait(myDrvier, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

# myDrvier.find_element_by_xpath('//*[@id="u"]').send_keys('604183841')
# myDrvier.find_element_by_xpath('//*[@id="p"]').send_keys('NEWLIFE1992')

myDriver.find_element(By.XPATH, '//*[@id="u"]').send_keys('604183841')
myDriver.find_element(By.XPATH, '//*[@id="p"]').send_keys('NEWLIFE1992')

myDrvier.find_element_by_id("login_button").click()

time.sleep(5)

myDrvier.quit()

