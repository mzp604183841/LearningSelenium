from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Page(object):
    login_url = 'http://www.126.com'

    def __init__(self, webdriver, base_url=login_url):
        self.driver = webdriver
        self.base_url = base_url
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    url = '/'

    # 定位器
    username_loc = (By.ID, 'idInput')
    password_loc = (By.ID, 'pwdInput')
    submit_log = (By.ID, 'LoginBtn')

    # Action
    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.password_loc).click()


def test_uers_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()


def main():
    try:
        driver = webdriver.Chrome()
        username = '604183841'
        password = 'qwe@123qwe'
        test_uers_login(driver, username, password)
        time.sleep(3)
        text = driver.find_element_by_xpath("//span[@id='spnUid']").text
        assert (text == '604183841@126.com'), '用户名称不匹配，登录失败'
    finally:
        driver.close()


if __name__ == '__main__':
    main()
