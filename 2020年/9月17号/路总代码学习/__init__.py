from selenium import webdriver
from selenium.webdriver.chrome.options import Options

global driver


def setUpDriver(self):
    # 先定义一个自己的选项卡，
    my_options = Options()
    # 定义一个模拟器
    mobile_emulation = {'deviceName': 'iPhone 6/7/8'}
    # 在自己的选项卡里，把模拟器选项添加进去
    my_options.add_experimental_option('mobileEmulation', mobile_emulation)
    # 把这个选项卡作为参数，生成自己的driver
    my_driver = webdriver.Chrome(chrome_options=my_options)
    # 设置driver的隐式等待时间为5秒
    my_driver.implicitly_wait(5)

    base_url = "https://www.douban.com/"
    my_driver.get(base_url)

    return my_driver


driver = setUpDriver()
