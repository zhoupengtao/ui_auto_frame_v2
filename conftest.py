# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 9:15
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : conftest.py
# @Software: PyCharm

import pytest
import logging
from selenium import webdriver
from selenium.webdriver import Remote

# 定义钩子函数hook进行命令行定义传参
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="browser option: firefox or chrome")


# 定义钩子函数hook进行测试用例name和_nodeid输出
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        logging.info(item.name)
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")
        logging.info(item._nodeid)

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
def session_remote_driver(request):
    browser = request.config.getoption("--browser")
    print("获取命令行传参：{}".format(request.config.getoption("--browser")))
    driver = Remote(command_executor="http://127.0.0.1:4444/wd/hub",
                    desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '',
                                          'javascriptEnabled': True})
    yield driver
    #driver.close()
    driver.quit()