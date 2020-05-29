# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 22:53
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm
import os
import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from PageObject.login_page import Login_page
from PageObject.buy_page import Buy_page
from PageObject.register_page import Register_page
from Common.publicMethod import PubMethod
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope="function")
# def session_driver(request):
#     print("获取命令行传参：{}".format(request.config.getoption("--browser")))
#     # 不开启浏览器设置
#     # chrome_options = Options()
#     # chrome_options.add_argument('--headless')
#     # driver = webdriver.Chrome(chrome_options=chrome_options)
#     # driver = webdriver.Chrome()
#     driver = webdriver.Firefox()
#     yield driver
#     driver.close()
#     driver.quit()


@pytest.fixture(scope="function")
def login_page_class_load(session_remote_driver):
    login_page = Login_page(session_remote_driver)
    yield login_page


@pytest.fixture(scope="function")
def buy_page_class_load(session_remote_driver):
    buy_page = Buy_page(session_remote_driver)
    yield buy_page


@pytest.fixture(scope="function")
def buy_page_class_load(session_remote_driver):
    buy_page = Buy_page(session_remote_driver)
    yield buy_page

# if __name__ == '__main__':
#     session_remote_driver()
