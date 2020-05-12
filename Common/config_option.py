# coding:utf-8
import os
import configparser


# 封装配置文件的操作方法
class Config_option:

    # 获取项目路劲
    def project_path(self):
        return os.path.split(os.path.realpath(__file__))[0].split('C')[0]

    def config_url(self):
        config = configparser.ConfigParser()
        config.read(self.project_path() + "config.ini")
        print(self.project_path() + "config.ini")
        return config.get("testUrl", "url")


if __name__ == "__main__":
    config = Config_option()
    print(config.config_url())
