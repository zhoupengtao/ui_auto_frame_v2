# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm
import os
import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from Common.publicMethod import PubMethod





# @pytest.fixture(scope="session")
# def session_remote_driver():
#     current_dir = os.path.dirname(__file__)
#     config_path = os.path.join(current_dir, "Conf", "config.yaml")
#     local_driver_conf = PubMethod.read_yaml(config_path)
#     local_driver_dir = local_driver_conf["local_driver_conf"]
#     print(local_driver_dir)
#     driver = Remote(command_executor=local_driver_dir["host"],
#                     desired_capabilities={'platform': 'ANY', 'browserName': local_driver_dir["browser"], 'version': '',
#                                           'javascriptEnabled': True})
#     yield driver
#     driver.close()
#     driver.quit()


# if __name__ == '__main__':
#     session_remote_driver()
