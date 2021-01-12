from selenium import webdriver
import unittest
import time


class Douban(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.homePage_handle = ''

    def test_locatedElements(self):
        self.driver.get('https://www.douban.com/')
        self.homePage_handle = self.driver.current_window_handle
        elements = self.driver.find_elements_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li')

        for element in elements:
            if element.text == '豆瓣读书':
                element.click()

        time.sleep(3)

        allPage_handles = self.driver.window_handles
        for handle in allPage_handles:
            if handle == self.homePage_handle:
                self.driver.switch_to.window(self.homePage_handle)
                print('现在切回到豆瓣首页')
        time.sleep(3)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
