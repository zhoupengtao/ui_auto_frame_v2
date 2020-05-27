# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
import os
import sys
import json
import yaml
import time
import pytest
import threading
from Common.publicMethod import PubMethod
from selenium.webdriver import Remote

root_dir = os.path.dirname(__file__)
config_yaml = PubMethod.read_yaml("./Conf/config.yaml")


def modify_report_environment_file(report_widgets_dir):
    """
    向environment.json文件添加测试环境配置，展现在allure测试报告中
    @return:
    """
    environment_info = [
        {"name": '测试地址', "values": [config_yaml['allure_environment']['URL']]},
        {"name": '测试版本号', "values": [config_yaml['allure_environment']["version"]]},
        {"name": '测试账户', "values": [config_yaml['allure_environment']['username']]},
        {"name": '测试说明', "values": [config_yaml['allure_environment']['description']]}
    ]
    # 确保目录存在
    PubMethod.create_dirs(os.path.join(report_widgets_dir, 'widgets'))
    with open('./Report/allure-results/widgets/environment.json', 'w', encoding='utf-8') as f:
        json.dump(environment_info, f, ensure_ascii=False, indent=4)


def run_all_case(browser):
    report_dir = os.path.abspath("./Report/{}".format(browser))
    report_widgets_dir = os.path.abspath("./Report/allure-results")
    # 定义测试用例集合
    # 定义features集合
    allure_features = ["--allure-features"]
    allure_features_list = ["Login_page_case"]
    allure_features_args = ",".join(allure_features_list)
    # 定义stories集合
    allure_stories = ["--allure-stories"]
    allure_stories_args = ['']
    allure_path_args = ['--alluredir', report_dir, '--clean-alluredir']
    test_args = ['-s', '-q', '--browser={}'.format(browser)]
    # 拼接运行参数
    run_args = test_args + allure_path_args + allure_features + allure_features_list + allure_stories + allure_stories_args
    # 使用pytest.main
    pytest.main(run_args)
    # 生成allure报告，需要系统执行命令--clean会清楚以前写入environment.json的配置
    cmd = 'allure generate ./Report/{} -o ./Report/{}/allure-results --clean'.format(browser.replace(" ", "_"), browser.replace(" ", "_"))
    print("cmd:{}".format(cmd))
    try:
        os.system(cmd)
    except Exception as e:
        print('命令【{}】执行失败！'.format(cmd))
        sys.exit()
    # 定义allure报告环境信息
    modify_report_environment_file(report_widgets_dir)
    # 打印url，方便直接访问
    url = '报告链接：http://127.0.0.1:63342/{}/Report/{}/allure-results/index.html'.format(root_dir.split('/')[-1], browser.replace(" ", "_"))
    print("输出项目跟目录{}".format(root_dir.split('/')[-1]))
    print(url)


def execute_selenium_cmd():
    # 需要启动三个进程，使用多线程
    try:
        # 启动hub节点,启动之前需要下载selenium-server-standalone，以及对应的browser的driver
        res = os.system('java -jar Selenium_server_dir\\selenium-server-standalone-3.141.0.jar -role hub')
        print(res)
        # 启动node节点,注册到hub节点，启动三个节点，适配三种浏览器，节点和浏览器的对应关系通过driver的remote的远程调用来进行，指定IP和browser
        os.system(
            "java -jar Selenium_server_dir\\selenium-server-standalone-3.141.0.jar -role node -port 5555 -hub http://localhost:4444/grid/register")
        os.system(
            "java -jar Selenium_server_dir\\selenium-server-standalone-3.141.0.jar -role node -port 5556 -hub http://localhost:4444/grid/register")
        os.system(
            "java -jar Selenium_server_dir\\selenium-server-standalone-3.141.0.jar -role node -port 5557 -hub http://localhost:4444/grid/register")
    except Exception as e:
        print("输出异常项：{}".format(e))


# test cmd dir_path
def receive_cmd_arg():
    global root_dir
    input_browser = sys.argv
    print(input_browser)
    if len(input_browser) > 1:
        try:
            if input_browser[1] == "chrome":
                root_dir.replace("\\", "/")
                root_dir = root_dir.replace("\\", "/")
                run_all_case("chrome")
            elif input_browser[1] == "firefox":
                print("进入firefox浏览器测试")
                root_dir = root_dir.replace("\\", "/")
                print("输出firefox_root_dir:{}".format(root_dir.replace("\\", "/")))
                run_all_case("firefox")
            elif input_browser[1] == "ie":
                root_dir.replace("\\", "/")
                root_dir = root_dir.replace("\\", "/")
                run_all_case("internet explorer")
            else:
                print("参数错误，请重新输入！！！")
        except Exception as e:
            print("命令行传参错误信息：{}".format(e))
    else:
        run_all_case("chrome")


if __name__ == "__main__":
    receive_cmd_arg()
