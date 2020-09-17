from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class baiduSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test_searchPython(self):
        element = self.driver.find_element_by_id('kw')
        element.send_keys('python')
        element.send_keys(Keys.RETURN)
        assert 'Not result found' not in self.driver.page_source
        time.sleep(3)

    def test_locateElements(self):
        # elements = self.driver.find_elements_by_class_name('mnav c-font-normal c-color-t')

        # //*[@id="s-top-left"]/a[4]

        elements = self.driver.find_elements_by_xpath('//*[@id="s-top-left"]')
        for element in elements:
            print(element.get_attribute('class'))


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
