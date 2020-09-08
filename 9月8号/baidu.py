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

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
