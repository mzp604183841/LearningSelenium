from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time
from selenium.webdriver import ActionChains


class CebbankApply(unittest.TestCase):
    def setUp(self) -> None:

        option = Options()
        mobile_emulation = dict(deviceName='iPhone 6/7/8')
        option.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(2)  # 设置隐式等待 2 秒
        self.actionChain = ActionChains(self.driver)

        self.driver.get('https://xyk.cebbank.com/icip/icip-applypage/info1?cardId=16159')
        try:
            assert self.driver.title == '中国光大银行信用卡卡'
        except Exception as error:
            print(error)
        finally:
            pass

    def test_info1_apply(self):
        chinese_name = self.driver.find_element_by_xpath('//*[@id="baseForm"]/div[1]/div/div[1]/div/input')
        chinese_name.send_keys('刘德华')

        id_num = self.driver.find_element_by_xpath('//*[@id="baseForm"]/div[3]/div/div[1]/div/input')
        id_num.send_keys('330101197507180013')

        mobile = self.driver.find_element_by_xpath('//*[@id="baseForm"]/div[4]/div/div[1]/div/input')
        mobile.send_keys('13120000001')

        verifyCode_button = self.driver.find_element_by_xpath('//*[@id="codeContainer"]/button/div')
        verifyCode_button.click()

        verifyCode = self.driver.find_element_by_xpath('//*[@id="codeContainer"]/div/div/div[1]/div/input')
        verifyCode.send_keys('123123')

        image_2 = self.driver.find_element_by_xpath('//*[@id="cardGroup"]/div/div[1]/div/img')
        self.actionChain.context_click(image_2).perform()
        image_2.is_displayed()
        # city_select = self.driver.find_element_by_xpath('//*[@id="baseForm"]/div[6]')
        # city_select.click()

        time.sleep(4)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
