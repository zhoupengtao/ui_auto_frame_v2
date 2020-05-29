# coding:utf-8
import unittest
from selenium import webdriver
from PageObject.login_page import Login_page
from PageObject.buy_page import Buy_page
from selenium.webdriver.chrome.options import Options
import pytest
import allure
import inspect
import logging
from selenium import webdriver
from PageObject.login_page import Login_page
from Common.publicMethod import PubMethod


@allure.feature("Login_page_case")
class Test_Login_page_case:

    @allure.story("Login")
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.link("https://www.baidu.com", name="连接跳转百度")
    @allure.testcase("https://www.sina.com", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    def test_DLZC1(self, login_page_class_load, session_remote_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        login_page_class_load.login_by_config_url()
        username_input_attribute_value = login_page_class_load.get_username_attribute_value()
        try:
            assert username_input_attribute_value == "邮箱/手机号码"
        except Exception as e:
            print("测试用例执行失败：{}".format(e))
            PubMethod.screen_picture(session_remote_driver)

    @allure.story("Login")
    @allure.severity("normal")
    @allure.title("test")
    def test_DLZC2(self, login_page_class_load):
        login_page_class_load.login_by_config_url()
        login_page_class_load.click_reset_btn()
        reset_title = login_page_class_load.get_reset_page_title()
        assert reset_title == "找回密码"

    @allure.story("Login")
    @allure.severity("normal")
    @allure.title("test")
    def test_DLZC3(self, login_page_class_load):
        login_page_class_load.login_by_config_url()
        login_page_class_load.click_register_btn()
        register_title = login_page_class_load.get_register_page_title()
        assert register_title == "注册"

    @allure.story("Login")
    @allure.severity("normal")
    @allure.title("test")
    def test_DLZC4(self, login_page_class_load):
        login_page_class_load.login_by_config_url()
        login_page_class_load.click_login_btn()
        error_text = login_page_class_load.get_error_text()
        assert error_text == "帐号不能为空"

    @allure.story("Login")
    @allure.severity("normal")
    @allure.title("test")
    def test_DLZC5(self, login_page_class_load):
        login_page_class_load.login_by_config_url()
        login_page_class_load.username_send_keys(1)
        login_page_class_load.click_login_btn()
        error_text = login_page_class_load.get_error_text()
        assert error_text == "密码不能为空"

    @allure.story("Login")
    @allure.severity("normal")
    @allure.title("test")
    def test_DLZC6(self, login_page_class_load):
        login_page_class_load.login_by_config_url()
        login_page_class_load.username_send_keys("1")
        login_page_class_load.password_send_keys("1")
        login_page_class_load.click_login_btn()
        error_text = login_page_class_load.get_error_text()
        assert error_text == "账号不存在"

    @allure.story("Login")
    @allure.severity("normal")
    @allure.title("test")
    def test_DLZC7(self, login_page_class_load):
        login_page_class_load.login_by_config_url()
        login_page_class_load.username_send_keys("13199044512")
        login_page_class_load.password_send_keys("1")
        login_page_class_load.click_login_btn()
        error_text = login_page_class_load.get_error_text()
        assert error_text == "密码错误"

    @allure.story("Login")
    @allure.severity("normal")
    @allure.title("test")
    def test_DLZC8(self, login_page_class_load):
        login_page_class_load.login_by_config_url()
        login_page_class_load.username_send_keys("13199044512")
        login_page_class_load.password_send_keys("123")
        login_page_class_load.click_login_btn()
        btn_buy_text = self.buy_page.find_button_buy()
        assert btn_buy_text == "购买"

    @allure.story("Login")
    @allure.severity("normal")
    @allure.title("test")
    def test_DLZC9(self, login_page_class_load):
        login_page_class_load.login_by_config_url()
        login_page_class_load.username_send_keys("test1@qq.com")
        login_page_class_load.password_send_keys("123")
        login_page_class_load.click_login_btn()
        btn_buy_text = self.buy_page.find_button_buy()
        assert btn_buy_text == "购买"


if __name__ == "__main__":
    pytest.main(["test_login_page_case.py"])
