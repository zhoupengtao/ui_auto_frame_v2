# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
import os
import sys
import pytest
import allure
root_dir = os.path.dirname(__file__)
if __name__ == "__main__":
    report_dir = os.path.abspath("./Reports")
    #定义测试用例集合
    #定义features集合
    allure_features = ["--allure-features"]
    allure_features_list = ["Login_page_case"]
    allure_features_args = ",".join(allure_features_list)
    #定义stories集合
    allure_stories = ["--allure-stories"]
    allure_stories_args = ['']
    allure_path_args = ['--alluredir', report_dir, '--clean-alluredir']
    test_args = ['-s', '-q']
    #拼接运行参数
    run_args = test_args + allure_path_args + allure_features + allure_features_list + allure_stories + allure_stories_args
    #使用pytest.main
    pytest.main(run_args)
    #生成allure报告，需要系统执行命令
    cmd = 'allure generate ./Reports/ -o ./Report/allure-results  --clean'
    try:
        os.system(cmd)
    except Exception as e:
        print('命令【{}】执行失败！'.format(cmd))
        sys.exit()
    # 打印url，方便直接访问
    url = '报告链接：http://127.0.0.1:63342/{}/Report/allure-results/index.html'.format(root_dir.split('/')[-1])
    print(url)
