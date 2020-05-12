# coding:utf-8
from Base.base import Base
from selenium.webdriver.common.by import By


# 封装速涡手游加速器注册页面操作对象及各个元素及操作方法
class Register_page(Base):
    def get_username_attribute_value(self):
        """
            获得账号输入框的placeholder值
        @return: 获得账号输入框的placeholder值
        """
        return super().get_placeholder((By.NAME, "Username"))

    def get_password_attribute_value(self):
        """
            获得密码输入框的placeholder值
        @return: 获得密码输入框的placeholder值
        """
        return super().get_placeholder((By.NAME, "Password"))

    def get_code_attribute_value(self):
        """
            获得验证码输入框的placeholder值
        @return: 获得验证码输入框的placeholder值
        """
        return super().get_placeholder((By.NAME, "code"))

    def find_button_other_register(self):
        """
            查找海外注册按钮
        @return: 海外注册按钮文本值
        """
        return super().get_text((By.CLASS_NAME, "InputWarningA"))

    def find_button_register(self):
        """
            查找注册按钮
        @return: 注册按钮文本值
        """
        return super().get_text((By.CLASS_NAME, "RegisterBtn"))

    def find_button_login(self):
        """
            查找登录按钮文本值
        @return: 登录按钮文本值
        """
        return super().get_text((By.LINK_TEXT, "登录"))

    def find_button_code(self):
        """
            查找验证码按钮文本值
        @return: 验证码按钮文本值
        """
        return super().get_text((By.CLASS_NAME, "RegisterSendCode"))

    def click_other_register_btn(self):
        """
            点击海外用户注册登录按钮
        """
        super().click_btn((By.LINK_TEXT, "海外用户注册"))

    def check_page_is_other_page(self):
        """
            海外用户登录界面检查，检查select元素是否存在
        @return: TRUE/FALSE
        """
        return super().check_select_is_existence((By.CLASS_NAME, "country-code"))

    def click_login_btn(self):
        """
            登录按钮点击
        """
        super().click_btn((By.LINK_TEXT, "登录"))

    def get_login_page_title(self):
        """
            获取登录页面的title
        @return: title
        """
        return super().get_text((By.CLASS_NAME, "InputTitleText"))

    def click_register_btn(self):
        """
            点击注册按钮
        """
        super().click_btn((By.CLASS_NAME, "RegisterBtn"))

    def click_code_btn(self):
        """
            点击发送验证码按钮
        """
        super().click_btn((By.LINK_TEXT, "发送验证码"))

    def get_error_text(self):
        """
            获得输入框输入错误的返回信息
        @return: 获得输入框输入错误的返回信息
        """
        return super().get_text((By.XPATH, "/html/body/div[2]/form/div[1]/span"))

    def username_send_keys(self, value):
        """
            输入账号输入框的值
        @param value: value
        """
        super().send_key((By.NAME, "Username"), value)

    def password_send_keys(self, value):
        """
            输入密码输入框的值
        @param value: value
        """
        super().send_key((By.NAME, "Password"), value)

    def code_send_keys(self, value):
        """
            输入验证码输入框的值
        @param value: value
        """
        super().send_key((By.NAME, "code"), value)
