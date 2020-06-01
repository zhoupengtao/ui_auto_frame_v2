# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 9:49
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : start_server_docker.py
# @Software: PyCharm
import docker
import datetime
import os
import json
from Common.publicMethod import PubMethod

# 读取selenium配置文件
selenium_config_path = os.path.join(os.path.dirname(__file__), "Conf", "selenium_config.yaml")
selenium_config = PubMethod.read_yaml(selenium_config_path)


def remove_container(client):
    """
    删除之前残留的以selenium开头的测试容器
    :param docker_info: 配置文件读取的docker信息
    :return:
    """
    for item in client.containers.list():
        print(item.attrs["Config"]["Image"])
        try:
            # 停止所有selenium开头的容器，并且删除容器
            if "selenium" in item.attrs["Config"]["Image"]:
                item.stop()
                item.remove()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                      '%s容器删除成功！' % selenium_config["selenium_config"]['selenium_hub_url'],
                      item.short_id)
        except Exception as e:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  '%s容器删除失败！' % selenium_config["selenium_config"]['selenium_hub_url'],
                  item.short_id)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          '%s所有容器删除成功！' % selenium_config["selenium_config"]['selenium_hub_url'])


def check_images(client):
    images = client.images.list()
    need_images_list = ["selenium/hub", "selenium/node-firefox", "selenium/node-chrome", "selenium/node-chrome-debug",
                        "selenium/node-firefox-debug", "selenium/standalone-chrome-debug",
                        "selenium/standalone-firefox-debug"]
    for need_image in need_images_list:
        for image in images:
            if str(image).find(str(need_image)) != -1:
                print("包含该镜像：{}".format(image))
            else:
                print("不包含该镜像：{}".format(need_image))
                try:
                    client.images.pull(need_image, tag="latest")
                except Exception as e:
                    print("镜像拉取失败，失败信息为：{}".format(e))


def start_server(client, selenium_config):
    # 启动hub节点
    hub_info = selenium_config["selenium_config"]["docker_image"]["hub"]
    print(hub_info)
    res = client.containers.run(
        image=hub_info['image'],
        detach=True,
        tty=True,
        stdin_open=True,
        restart_policy={'Name': 'always'},
        name=hub_info['name'],
        privileged=True,
        ports={
            '4444/tcp': int(hub_info['port'])
        }
    )
    print(res)
    # 启动node-chrome节点
    node_chrome_info = selenium_config["selenium_config"]["docker_image"]["node-chrome"]
    print(node_chrome_info)
    res1 = client.containers.run(
        image=node_chrome_info['image'],
        detach=True,
        tty=True,
        stdin_open=True,
        restart_policy={'Name': 'always'},
        name=node_chrome_info['name'],
        privileged=True,
        links={'hub': 'hub'},
        ports={
            '5555/tcp': int(node_chrome_info['port'])
        }
    )
    print(res1)
    # 启动node-firefox节点
    node_firefox_info = selenium_config["selenium_config"]["docker_image"]["node-firefox"]
    print(node_firefox_info)
    res2 = client.containers.run(
        image=node_firefox_info['image'],
        detach=True,
        tty=True,
        stdin_open=True,
        restart_policy={'Name': 'always'},
        name=node_firefox_info['name'],
        privileged=True,
        links={'hub': 'hub'},
        ports={
            '5556/tcp': int(node_firefox_info['port'])
        }
    )
    print(res2)
    # 启动node调试模式节点
    node_chrome_debug_info = selenium_config["selenium_config"]["docker_image"]["node-chrome-debug"]
    print(node_chrome_debug_info)
    client.containers.run(
        image=node_chrome_debug_info['image'],
        detach=True,
        tty=True,
        stdin_open=True,
        restart_policy={'Name': 'always'},
        name=node_chrome_debug_info['name'],
        privileged=True,
        links={'hub': 'hub'},
        ports={
            '5900/tcp': int(node_chrome_debug_info['port'])
        }
    )


if __name__ == '__main__':
    # 建立docker客户端连接
    client = docker.DockerClient(selenium_config['selenium_config']['docker_url'])
    # 清理原有的selenium的docker容器
    remove_container(client)
    # 检查docker本地镜像仓库是否含有selenium的docker镜像
    # check_images(client)
    # 启动selenium的hub节点和node节点
    start_server(client, selenium_config)
