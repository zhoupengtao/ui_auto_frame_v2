# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 10:05
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : test_remote_selenium_container.py
# @Software: PyCharm
# coding=utf-8

from selenium import webdriver

chrome_capabilities = {
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    # "marionette": True,
}
browser = webdriver.Remote("http://10.5.16.224:4444/wd/hub", desired_capabilities=chrome_capabilities)
browser.get("http://www.163.com")
browser.get_screenshot_as_file(r"D:/sample/chrome.png")
browser.quit()
