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


@pytest.fixture(scope="session")
def session_driver():
    # 不开启浏览器设置
    # chrome_options=Options()
    # chrome_options.add_argument('--headless')
    # self.driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope="session")
def session_remote_driver():
    current_dir = os.path.dirname(__file__)
    print(current_dir)
    config_path = os.path.join(current_dir, "Conf", "config.yaml")
    print(config_path)
    local_distributed_config = PubMethod.read_yaml(config_path)
    distributed_config_dic = local_distributed_config["local_distributed_config"]
    print(distributed_config_dic)
    for host, browser in distributed_config_dic.items():
        print(host)
        print(browser)
        driver = Remote(command_executor=host["host"],
                        desired_capabilities={'platform': 'ANY', 'browserName': browser["browser"], 'version': '',
                                              'javascriptEnabled': True})
        yield driver
        driver.close()
        driver.quit()


if __name__ == '__main__':
    session_remote_driver()
