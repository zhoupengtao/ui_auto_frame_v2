# coding:utf-8
import unittest
from selenium import webdriver
from PageObject.login_page import Login_page
from PageObject.buy_page import Buy_page
from PageObject.register_page import Register_page
from Common.log_option import log,log_INFO,log_ERROR,log_DEBUG,log_WARNING


class Register_page_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log_WARNING("类前执行一次")

    @classmethod
    def tearDownClass(cls):
        log_WARNING("类后执行一次")

    def setUp(self):
        log_WARNING("开始执行case")
        self.driver = webdriver.Chrome()
        self.login_page = Login_page(self.driver)
        self.buy_page = Buy_page(self.driver)
        self.register_page = Register_page(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        log_WARNING("结束执行case")

    def test_DLZC10(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        username_input_attribute_value = self.register_page.get_username_attribute_value()
        password_input_attribute_value = self.register_page.get_password_attribute_value()
        code_input_attirbute_value = self.register_page.get_code_attribute_value()
        code_btn_text = self.register_page.find_button_code()
        register_btn_text = self.register_page.find_button_register()
        other_register_btn_text = self.register_page.find_button_other_register()
        login_btn_text = self.register_page.find_button_login()
        self.assertEqual(username_input_attribute_value, "手机号码")
        self.assertEqual(password_input_attribute_value, "密码")
        self.assertEqual(code_input_attirbute_value, "验证码")
        self.assertEqual(code_btn_text, "发送验证码")
        self.assertEqual(register_btn_text, "注册")
        self.assertEqual(other_register_btn_text, "海外用户注册")
        self.assertEqual(login_btn_text, "登录")

    def test_DLZC11(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.click_other_register_btn()
        res = self.register_page.check_page_is_other_page()
        self.assertTrue(res)

    def test_DLZC12(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.click_login_btn()
        login_title = self.register_page.get_login_page_title()
        self.assertEqual(login_title, "登录")

    def test_DLZC13(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.click_register_btn()
        error_text = self.register_page.get_error_text()
        self.assertEqual(error_text, "手机号不能为空")

    def test_DLZC14(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.click_code_btn()
        error_text = self.register_page.get_error_text()
        self.assertEqual(error_text, "用户名不能为空")

    def test_DLZC15(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.username_send_keys(1)
        self.register_page.click_register_btn()
        error_text = self.register_page.get_error_text()
        self.assertEqual(error_text, "手机号码格式不正确")

    def test_DLZC16(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.username_send_keys("11111111111")
        self.register_page.click_register_btn()
        error_text = self.register_page.get_error_text()
        self.assertEqual(error_text, "验证码不能为空")

    def test_DLZC17(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.username_send_keys("13199044512")
        self.register_page.click_code_btn()
        error_text = self.register_page.get_error_text()
        self.assertEqual(error_text, "该手机号已经注册过帐号")

    def test_DLZC18(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.username_send_keys("11111111111")
        self.register_page.code_send_keys("123")
        self.register_page.click_register_btn()
        error_text = self.register_page.get_error_text()
        self.assertEqual(error_text, "密码不能为空")

    def test_DLZC19(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        self.register_page.username_send_keys("11111111111")
        self.register_page.password_send_keys("123")
        self.register_page.code_send_keys("123")
        self.register_page.click_register_btn()
        error_text = self.register_page.get_error_text()
        self.assertEqual(error_text, "请先获取验证码")


if __name__ == "__main__":
    unittest.main()
