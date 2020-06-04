# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 9:14
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : test_script.py
# @Software: PyCharm
import os
import logging
from Common.publicMethod import PubMethod
from PageObject.elem_params import Login_page_elem
from selenium.webdriver.common.by import By
login_elem_data = os.path.join(os.path.dirname(__file__), "Login_page.yaml")


def get_elem(login_elem_data, elem_name):
    elems_info = PubMethod.read_yaml(login_elem_data)
    print(elems_info)
    for item in elems_info["parameters"]:
        if item["elem_name"] == elem_name:
            elem_locator = ("By.{}".format(item["data"]["method"]), item["data"]["value"])
            method = item["data"]["method"]
            value = item["data"]["value"]
            print(method)
            print(value)
            logging.info("元素定位方式为：{}，元素对象值为：{}".format(method, value))
            if method == "ID" and value is not None:
                return elem_locator
            elif method == "XPATH" and value is not None:
                return elem_locator
            elif method == "LINK_TEXT" and value is not None:
                return elem_locator
            elif method == "PARTIAL_LINK_TEXT" and value is not None:
                return elem_locator
            elif method == "NAME" and value is not None:
                return elem_locator
            elif method == "TAG_NAME" and value is not None:
                return elem_locator
            elif method == "CLASS_NAME" and value is not None:
                return elem_locator
            elif method == "CSS_SELECTOR" and value is not None:
                return elem_locator
            else:
                logging.error("该定位方式异常，定位元素值异常，请检查！！！")


if __name__ == '__main__':

    log_obj = Login_page_elem()
    elem = log_obj.get_locator("Password")
    print(elem)
    print(type(By.NAME))
    #print(type(elem[0]))
    print(type(elem))


