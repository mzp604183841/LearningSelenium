from selenium import webdriver
from selenium.webdriver.chrome.options import Options

myOption = Options()
# myOpiton.page_load_strategy = 'normal'
myOption.page_load_strategy = 'eager'
myDriver = webdriver.Chrome('/Users/MZP/Desktop/chromedriver', options=myOption)

myDriver.get('http://www.baidu.com')
myDriver.quit()
