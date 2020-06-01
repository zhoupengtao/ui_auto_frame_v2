# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import logging
from Common.config_option import Config_option
from Common.publicMethod import PubMethod

#conf_path = os.path.join(os.path.dirname(__file__).rsplit("/", 2)[0], "Conf", "config.yaml")
conf_path = os.path.abspath("./Conf/config.yaml")
# Base层封装的是元素的操作方法
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
        try:
            self.driver.get(url)
            logging.info("{}获取成功".format(url))
        except Exception as e:
            logging.error("URL获取失败，错误信息为：{}".format(e))

    def get_login_url_from_config(self):
        """

        @return: 配置文件URL
        """
        config_info = PubMethod.read_yaml(conf_path)
        print("config_info地址：{}".format(config_info))
        return config_info["test_info"]["test_URL"]

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
            logging.error('locator参数类型错误，必须传元祖类型：locator=(By.XX,"value")')
        else:
            logging.info("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            try:
                time.sleep(2)
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_element(*locator))
                logging.info("元素对象为：{}".format(elem))
                return elem
            except:
                logging.error("定位不到元素")
                return print("定位不到元素")

    def find_elements(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象列表
        """
        try:
            elems = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(lambda x: x.find_elements(*locator))
            logging.info("元素组对象为：{}".format(elems))
        except Exception as e:
            logging.error("元素组对象获取失败，错误信息为：{}".format(e))
        return elems

    def switch_to_frame(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return:
        """
        elem = self.find_element(locator)
        try:
            self.driver.switch_to.frame(elem)
            logging.info("frame切换成功")
        except Exception as e:
            logging.error("frame切换失败，错误信息为：{}".format(e))

    def switch_to_handle(self, index):
        """
            切换窗口句柄
        """
        # 获取当前所有窗口句柄
        try:
            handles = self.driver.window_handles
            logging.info("获取当前所有窗口句柄成功，句柄对象列表为：{}".format(handles))
        except Exception as e:
            logging.error("获取当前所有窗口句柄失败，错误信息为：{}".format(e))
        # 切换到新窗口句柄
        try:
            self.driver.switch_to.window(handles[index])
            logging.info("切换新窗口句柄成功，切换窗口的索引index为：{}".format(index))
        except Exception as e:
            logging.error("切换新窗口句柄失败，错误信息为：{}".format(e))

    def send_key(self, locator, value):
        """

        @param locator: 定位器
        @param value: value
        """
        elem = self.find_element(locator)
        try:
            elem.send_keys(value)
            logging.info("元素对象输入值成功，值为：{}".format(value))
        except Exception as e:
            logging.error("元素对象输入值失败，错误信息为：{}".format(e))

    def click_btn(self, locator):
        """

        @param locator: 定位器
        """
        elem = self.find_element(locator)
        try:
            elem.click()
            logging.info("元素对象点击成功")
        except Exception as e:
            logging.error("元素对象点击失败，错误信息为：{}".format(e))

    def get_text(self, locator):
        """

        @param locator:定位器
        @return:元素文本值
        """
        elem = self.find_element(locator)
        try:
            elem_text = elem.text
            logging.info("元素text值：{}".format(elem_text))
        except Exception as e:
            logging.error("元素text获取失败，错误信息为：{}".format(e))
        return elem_text

    def get_text_by_elements(self, locator, index):
        """

        @param locator: 定位器
        @return: 返回定位对象组的第一个元素的值
        """
        elem = self.find_elements(locator)
        try:
            elem_text = elem[index].text
            logging.info("获取元素组对象，索引位置{}的值成功，值为：{}".format(index, elem_text))
        except Exception as e:
            logging.error("获取元素组对象，索引位置{}的值失败，失败信息为：{}".format(e))
        return elem_text

    def get_placeholder(self, locator):
        """

        @param locator: 定位器
        @return: 返回placeholder属性值
        """
        elem = self.find_element(locator)
        try:
            elem_placeholder_text = elem.get_attribute("placeholder")
            logging.info("该元素对象获取placeholder成功，placeholder值为：{}".format(elem_placeholder_text))
        except Exception as e:
            logging.error("该元素对象获取placeholder失败，错误信息为：{}".format(e))
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
    print(conf_path)
    config_info = PubMethod.read_yaml(conf_path)
    print(config_info["test_info"])