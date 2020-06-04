# coding:utf-8
from Base.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from PageObject.elem_params import Login_page_elem


# 封装速涡手游加速器登录页面操作对象及各个元素及操作方法
class Login_page(Base):
    def __init__(self, driver):
        self.elem_locator = Login_page_elem()
        super().__init__(driver)

    def login_by_config_url(self):
        """
            从配置文件config.ini获取登录地址
        @return: 登录地址
        """
        return super().login_by_config_url()

    def get_home_page_url(self, url):
        """
            登录测试地址URL
        @param url: 登录页面URL
        """
        self.get_url(url)

    def get_username_attribute_value(self):
        """
            获得账号输入框的placeholder值
        @return: 获得账号输入框的placeholder值
        """
        elem = self.elem_locator.get_locator("Username")
        return super().get_placeholder(elem)

    def get_password_attribute_value(self):
        """
            获得密码输入框的placeholder值
        @return:获得密码输入框的placeholder值
        """
        elem = self.elem_locator.get_locator("Password")
        return super().get_placeholder(elem)

    def find_button_reset_password(self):
        """
            查找忘记密码按钮
        @return:忘记密码按钮文本值
        """
        elem = self.elem_locator.get_locator("GoResetPassword")
        return super().get_text(elem)

    def find_button_login(self):
        """
            查找登录按钮
        @return:登录按钮文本值
        """
        elem = self.elem_locator.get_locator("LoginBtn")
        return super().get_text(elem)

    def find_button_register(self):
        """
            查找注册按钮
        @return: 注册按钮文本值
        """
        elem = self.elem_locator.get_locator("InputWarningA")
        return super().get_text(elem)

    def click_login_btn(self):
        """
            点击登录按钮
        """
        elem = self.elem_locator.get_locator("LoginBtn")
        super().click_btn(elem)

    def click_reset_btn(self):
        """
            点击忘记密码按钮
        """
        elem = self.elem_locator.get_locator("GoResetPassword")
        super().click_btn(elem)

    def click_register_btn(self):
        """
            点击注册按钮
        """
        elem = self.elem_locator.get_locator("InputWarningA")
        super().click_btn(elem)

    def get_reset_page_title(self):
        """
            获得找回密码页面的title
        @return:title
        """
        elem = self.elem_locator.get_locator("InputTitleText")
        return super().get_text(elem)

    def get_register_page_title(self):
        """
            获得注册页面的title
        @return:title
        """
        elem = self.elem_locator.get_locator("InputTitleText")
        return super().get_text(elem)

    def get_error_text(self):
        """
            获得输入框输入错误的返回信息
        @return: 获得输入框输入错误的返回信息
        """
        elem = self.elem_locator.get_locator("errorText")
        return super().get_text(elem)

    def username_send_keys(self, value):
        """
            输入账号输入框的值
        @param value: value
        """
        elem = self.elem_locator.get_locator("Username")
        super().send_key(elem, value)

    def password_send_keys(self, value):
        """
            输入密码输入框的值
        @param value: value
        """
        elem = self.elem_locator.get_locator("Password")
        super().send_key(elem, value)


if __name__ == "__main__":
    home_page = Login_page(webdriver.Chrome())
    home_page.login_by_config_url()
    print(home_page.find_button_login())
