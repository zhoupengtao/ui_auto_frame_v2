# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def session_driver():
        #不开启浏览器设置
        # chrome_options=Options()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        driver = webdriver.Chrome()
        yield driver
        driver.close()
        driver.quit()
