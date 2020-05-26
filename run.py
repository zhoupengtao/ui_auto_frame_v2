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
    test_args = ['-s', '-q']
    # 拼接运行参数
    run_args = test_args + allure_path_args + allure_features + allure_features_list + allure_stories + allure_stories_args
    # 使用pytest.main
    pytest.main(run_args)
    # 生成allure报告，需要系统执行命令--clean会清楚以前写入environment.json的配置
    cmd = 'allure generate ./Report/{} -o ./Report/{}/allure-results --clean'.format(browser, browser)
    print("cmd:{}".format(cmd))
    try:
        os.system(cmd)
    except Exception as e:
        print('命令【{}】执行失败！'.format(cmd))
        sys.exit()
    # 定义allure报告环境信息
    modify_report_environment_file(report_widgets_dir)
    # 打印url，方便直接访问
    url = '报告链接：http://127.0.0.1:63342/{}/Report/{}/allure-results/index.html'.format(root_dir.split('/')[-1], browser)
    print(url)


# 多线程+分布式执行selenium代码
def multi_threading_execute(node_count, host_path, browser_version):
    # 创建线程锁
    thread_lock.acquire()
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, "Conf", "config.yaml")
    local_driver_conf = PubMethod.read_yaml(config_path)
    local_driver_dir = local_driver_conf["local_driver_conf"]
    local_driver_dir["node"] = node_count
    local_driver_dir["host"] = host_path
    local_driver_dir["browser"] = browser_version
    print(local_driver_conf)
    with open(config_path, 'w', encoding="utf-8") as fw:
        yaml.dump(local_driver_conf, fw, encoding="utf-8")
        fw.close()

    run_all_case(browser_version)
    thread_lock.release()


def execute_selenium_cmd():
    # 需要启动三个进程，使用多线程
    try:
        # 启动hub节点,启动之前需要下载selenium-server-standalone，以及对应的browser的driver
        res = os.system('java -jar Selenium_server_dir\\selenium-server-standalone-3.141.0.jar -role hub')
        print(res)
        # 启动node节点,注册到hub节点，启动三个节点，适配三种浏览器，节点和浏览器的对应关系通过driver的remote的远程调用来进行，指定IP和browser
        os.system("java -jar Selenium_server_dir\\selenium-server-standalone-3.141.0.jar -role node -port 5555 -hub http://localhost:4444/grid/register")
        os.system("java -jar Selenium_server_dir\\selenium-server-standalone-3.141.0.jar -role node -port 5556 -hub http://localhost:4444/grid/register")
        os.system("java -jar Selenium_server_dir\\selenium-server-standalone-3.141.0.jar -role node -port 5557 -hub http://localhost:4444/grid/register")
    except Exception as e:
        print("输出异常项：{}".format(e))


if __name__ == "__main__":
    # run_all_case()
    # execute_selenium_cmd()
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, "Conf", "config.yaml")
    local_distributed_config = PubMethod.read_yaml(config_path)
    distributed_config_dic = local_distributed_config["local_distributed_config"]
    # 创建线程池
    threads = []
    # 创建线程锁
    thread_lock = threading.Lock()
    for node, node_info in distributed_config_dic.items():
        th = threading.Thread(target=multi_threading_execute, args=(node, node_info["host"], node_info["browser"]))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
