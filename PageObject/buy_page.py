# coding:utf-8
from Base.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver


# 封装速涡手游加速器购买页面操作对象及各个元素及操作方法
class Buy_page(Base):

    def find_button_buy(self):
        return self.get_text_by_elements((By.CLASS_NAME, "ProductBuyBtn"))
