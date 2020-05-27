# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 9:15
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : conftest.py
# @Software: PyCharm

import pytest
from selenium import webdriver

# 定义钩子函数hook进行命令行定义传参
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="browser option: firefox or chrome")

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