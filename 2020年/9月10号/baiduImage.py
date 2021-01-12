from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains


class BaiduImageSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.actionChain = ActionChains(self.driver)

    def test_upload_image_search(self):
        self.driver.get('https://image.baidu.com/')
        upload_field = self.driver.find_element_by_xpath('//*[@id="stuurl"]')
        camera = self.driver.find_element_by_class_name('sttb')
        if camera.is_displayed():
            self.actionChain.click(camera).perform()
            imageFile_path = '/Users/MZP/Pictures/图片/夏美酱/20180126145111991199.jpg'
            upload_field.send_keys(imageFile_path)
            time.sleep(3)

        self.driver.get

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
