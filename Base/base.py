# coding:utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from Common.log_option import log, log_INFO, log_ERROR, log_DEBUG, log_WARNING
from Common.config_option import Config_option
from Common.file_option import File_option


# Base层封装的是元素的操作方法，会调用Common中封装好的基础方法
class Base:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.poll_frequency = 0.5
        self.config = Config_option()

    def get_url(self, url):
        """

        @param url: 测试url
        """
        self.driver.get(url)

    def get_login_url_from_config(self):
        """

        @return: 配置文件URL
        """
        return self.config.config_url()

    def login_by_config_url(self):
        """
            登录URL
        """
        self.driver.maximize_window()
        self.driver.get(self.get_login_url_from_config())

    def find_element(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象
        """
        # 方法二次封装Demo
        # WebDriverWait(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
        # elem = WebDriverWait(driver, timeout, t).until(lambda x: x.findElenmentById("name"))元素显示等待
        # locator定位器，locator(by,value)即是传入元素定位器和元素值)
        if not isinstance(locator, tuple):
            log_ERROR('locator参数类型错误，必须传元祖类型：locator=(By.XX,"value")')
        else:
            log_INFO("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            try:
                time.sleep(2)
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_element(*locator))
                return elem
            except:
                log_WARNING("定位不到元素")
                return print("定位不到元素")

    def find_elements(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象列表
        """
        elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(lambda x: x.find_elements(*locator))
        return elem

    def switch_to_frame(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return:
        """
        elem = self.find_element(locator)
        self.driver.switch_to.frame(elem)

    def switch_to_handle(self):
        """
            切换窗口句柄
        """
        # 获取当前所有窗口句柄
        handles = self.driver.window_handles
        # 切换到新窗口句柄
        self.driver.switch_to.window(handles[1])

    def send_key(self, locator, value):
        """

        @param locator: 定位器
        @param value: value
        """
        elem = self.find_element(locator)
        elem.send_keys(value)

    def click_btn(self, locator):
        """

        @param locator: 定位器
        """
        elem = self.find_element(locator)
        elem.click()

    def get_text(self, locator):
        """

        @param locator:定位器
        @return:元素文本值
        """
        elem = self.find_element(locator)
        elem_text = elem.text
        print("文本值输出")
        print(elem_text)
        return elem_text

    def get_text_by_elements(self, locator):
        """

        @param locator: 定位器
        @return: 返回定位对象组的第一个元素的值
        """
        elem = self.find_elements(locator)
        elem_text = elem[0].text
        return elem_text

    def get_placeholder(self, locator):
        """

        @param locator: 定位器
        @return: 返回placeholder属性值
        """
        elem = self.find_element(locator)
        elem_placeholder_text = elem.get_attribute("placeholder")
        return elem_placeholder_text

    def check_select_is_existence(self, locator):
        """

        @param locator: 定位器
        @return: 返回TRUE、FALSE
        """
        try:
            elem = self.find_element(locator)
            return True
        except Exception as e:
            return False




if __name__ == "__main__":
    base = Base(webdriver.Chrome())
    base.login_by_config_url()
    base.screen_picture()
