from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待包


class Action(object):

    def __init__(self, browser):
        # 这里定义了一个 分隔符，暂时还不完全理解它的作用
        self.separator = ','
        self.browser = browser

    def mzp_setup_browser(self, browser_name='CHROME'):
        my_options = Options()
        mobile_emulator = {'deviceName': 'iPhone 6/7/8'}
        my_options.add_experimental_option('mobileEmulator', mobile_emulator)

        self.browser = webdriver.Chrome(options=my_options)
        return self.browser

    # def mzp_close_browser(self):
    #     self.browser.close()
    #
    # def mzp_set_max_window(self):
    #     self.browser.maximize_window()
    #
    # def mzp_set_window_size(self, width, height):
    #     self.browser.set_window_size(width, height, self.browser)

    '''这里根据传进的字符串选择定位器'''
    '''返回值也是定位器, 是一个这样的(By.xx, value) 元祖'''

    def mzp_select_element(self, selector):
        if self.separator not in selector:
            return By.ID, selector

        # 传进来的selector是一个字符串
        # 用逗号作为分隔符 分别拿到前两个元素去掉空格，作为by和value这两个值，这是干嘛的呢
        selector_by = selector.split(self.separator)[0].strip()
        selector_value = selector.split(self.separator)[1].strip()

        # selector 字符串为什么会包含这些文本 ？？？？
        if selector_by == 'i' or selector_by == 'id':
            locator = (By.ID, selector_value)
        elif selector_by == 'n' or selector_by == 'name':
            locator = (By.NAME, selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            locator = (By.XPATH, selector_value)
        elif selector_by == 's' or selector_by == 'css_selector':
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            print('非法的元素定位器')

        return locator

    '''定位单个元素'''
    '''返回值是一个元素对象'''

    def mzp_local_element(self, selector):
        locator = self.mzp_select_element(selector)
        if locator is not None:
            try:
                print(locator)
                element = self.browser.find_element(*locator)
            except:
                # 如此看来，selector是一个代表元素的字符串吗 ？？？？
                raise Exception('定位 %s 元素失败' % selector)
        else:
            print('元素定位器不合法')
        return element

    '''定位多个元素'''
    '''返回值是一组元素对象'''

    def mzp_local_elements(self, selector):
        locator = self.mzp_select_element(selector)
        if locator is not None:
            try:
                print(locator)
                elements = self.browser.find_elements(*locator)
            except:
                raise Exception('定位 %s 元素组失败' % selector)
        else:
            print('元素定位器不合法')
        return elements

    '''打开页面'''

    def mzp_open_page(self, url):
        self.browser.get(url)
        time.sleep(2)
        if self.browser.current_url == url:
            print('浏览器打开的页面链接和给定的一致')
        else:
            raise Exception('浏览器打开链接后，地址发生变化')

    def mzp_find_element(self, driver, locator):
        pass

    '''自定义的键盘方法'''
    '''只是用了可自动选择定位器的方法，不用把定位找元素的代码暴露在外'''

    def mzp_send_keys(self, selector, text):
        element = self.mzp_local_element(selector)
        element.clear()
        element.send_keys(text)

    '''自定义的鼠标点击方法'''
    '''同上原则，不必将定位找元素的代码暴露在外'''

    def mzp_click(self, selector):
        element = self.mzp_local_element(selector)
        element.click()

# 以上所有的这个类的代码写完了
# 现在最大的问题是，为什么那个字符串selector能够代表一个元素可选择的定位方式，或者说其中包含能够定位到它的"方法关键字"
# 妈了个腿，我现在知道为啥他要这么写了。
# 基本都是xpath方式定位，但是确实 找元素的下一层实现就是self.find_element(by=By.XPATH, value=xpath)
# 这种方式还是相对简单一点吧
# # # # # # #
# 这里有一个xpath的注意点，相对路径 //前main加点 变成 .// 的定位方式
# 加点以后，可以指定到当前标签下，而非整个页面
