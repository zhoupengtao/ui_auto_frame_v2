# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 22:41
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : get_sys_cmd.py
# @Software: PyCharm
import sys
input_browser = sys.argv
print(type(input_browser))
try:
    if input_browser[1] == "chrome":
        print("chrome")
    elif input_browser[1] == "firefox":
        print("firefox")
    elif input_browser[1] == "ie":
        print("internet explorer")
    else:
        print("参数错误，请重新输入！！！")
except Exception as e:
    print("命令行传参错误信息：{}".format(e))
