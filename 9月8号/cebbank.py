from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time


class CebbankApply(unittest.TestCase):
    def setUp(self) -> None:

        option = Options()
        mobile_emulation = dict(deviceName='iPhone 6/7/8')
        option.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get('https://xyk.cebbank.com/icip/icip-applypage/info1?cardId=16159')

    def test_info1_apply(self):
        chinese_name = self.driver.find_element_by_xpath('//*[@id="baseForm"]/div[1]/div/div[1]/div/input')
        chinese_name.send_keys('刘德华')
        time.sleep(2)

        id_num = self.driver.find_element_by_xpath('//*[@id="baseForm"]/div[3]/div/div[1]/div/input')
        id_num.send_keys('14243119920314753X')
        time.sleep(2)

        mobile = self.driver.find_element_by_xpath('//*[@id="baseForm"]/div[4]/div/div[1]/div/input')
        mobile.send_keys('13120000000')
        time.sleep(2)

        verifyCode_button = self.driver.find_element_by_xpath('//*[@id="codeContainer"]/button/div')
        verifyCode_button.click()
        time.sleep(2)

        verifyCode = self.driver.find_element_by_xpath('//*[@id="codeContainer"]/div/div/div[1]/div/input')
        verifyCode.send_keys('123123')
        time.sleep(2)

        city_select = self.driver.find_element_by_xpath('//*[@id="baseForm"]/div[6]')
        city_select.click()

        time.sleep(4)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
