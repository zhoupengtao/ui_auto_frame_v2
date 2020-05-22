# coding:utf-8
import unittest
from selenium import webdriver
from PageObject.login_page import Login_page
from PageObject.buy_page import Buy_page
from Common.log_option import log, log_INFO, log_ERROR, log_DEBUG, log_WARNING
from selenium.webdriver.chrome.options import Options
import pytest
import allure
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
    def test_DLZC1(self, login_page_class_load, session_driver):
        print("开始登陆测试")
        print(login_page_class_load)
        login_page_class_load.login_by_config_url()
        username_input_attribute_value = login_page_class_load.get_username_attribute_value()
        # password_input_attribute_value = login_page.get_password_attribute_value()
        # reset_btn_text = login_page.find_button_reset_password()
        # login_btn_text = login_page.find_button_login()
        # register_btn_text = login_page.find_button_register()
        try:
            assert username_input_attribute_value != "邮箱/手机号码"
        except Exception as e:
            print("测试用例执行失败：{}".format(e))
            PubMethod.screen_picture(session_driver)
        # self.assertEqual(password_input_attribute_value, "密码")
        # self.assertEqual(reset_btn_text, "忘记密码？")
        # self.assertEqual(login_btn_text, "登录")
        # self.assertEqual(register_btn_text, "注册")

    # def test_DLZC2(self):
    #     self.login_page.login_by_config_url()
    #     self.login_page.click_reset_btn()
    #     reset_title = self.login_page.get_reset_page_title()
    #     self.assertEqual(reset_title, "找回密码")
    #
    # def test_DLZC3(self):
    #     self.login_page.login_by_config_url()
    #     self.login_page.click_register_btn()
    #     register_title = self.login_page.get_register_page_title()
    #     self.assertEqual(register_title, "注册")
    #
    # def test_DLZC4(self):
    #     self.login_page.login_by_config_url()
    #     self.login_page.click_login_btn()
    #     error_text = self.login_page.get_error_text()
    #     self.assertEqual(error_text, "帐号不能为空")
    #
    # def test_DLZC5(self):
    #     self.login_page.login_by_config_url()
    #     self.login_page.username_send_keys(1)
    #     self.login_page.click_login_btn()
    #     error_text = self.login_page.get_error_text()
    #     self.assertEqual(error_text, "密码不能为空")
    #
    # def test_DLZC6(self):
    #     self.login_page.login_by_config_url()
    #     self.login_page.username_send_keys("1")
    #     self.login_page.password_send_keys("1")
    #     self.login_page.click_login_btn()
    #     error_text = self.login_page.get_error_text()
    #     self.assertEqual(error_text, "账号不存在")
    #
    # def test_DLZC7(self):
    #     self.login_page.login_by_config_url()
    #     self.login_page.username_send_keys("13199044512")
    #     self.login_page.password_send_keys("1")
    #     self.login_page.click_login_btn()
    #     error_text = self.login_page.get_error_text()
    #     self.assertEqual(error_text, "密码错误")
    #
    # def test_DLZC8(self):
    #     self.login_page.login_by_config_url()
    #     self.login_page.username_send_keys("13199044512")
    #     self.login_page.password_send_keys("123")
    #     self.login_page.click_login_btn()
    #     btn_buy_text = self.buy_page.find_button_buy()
    #     print(btn_buy_text)
    #     self.assertEqual(btn_buy_text, "购买")
    #
    # def test_DLZC9(self):
    #     self.login_page.login_by_config_url()
    #     self.login_page.username_send_keys("test1@qq.com")
    #     self.login_page.password_send_keys("123")
    #     self.login_page.click_login_btn()
    #     btn_buy_text = self.buy_page.find_button_buy()
    #     print(btn_buy_text)
    #     self.assertEqual(btn_buy_text, "购买")


if __name__ == "__main__":
    pytest.main(["test_login_page_case.py"])
