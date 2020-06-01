### ui_auto_frame框架解释:

### 简介

**UI自动化测试框架：pytest+selenium+allure**

---

### 模块设计

**Base模块封装操作元素的公共方法**
**Check_config_script模块存放环境检查的脚本**
**Common模块是封装的读取配置文件的公共方法，类似于util工具类**
**Conf模块是存放全局配置文件**
**Grid_server模块存放selenium-server（hub和node）启动bat脚本，以及三种selenium三种浏览器命令行参数的入口**
**Logs模块，用于生成日志文件**
**PageObject模块提取页面对象封装公共操作方法**
**Report模块，存放测试报告，以及测试报告的生成模板allure**
**TestCases模块，用于存放测试case**

---

### allure装饰器

- @allure.severity("critical")
  - 优先级，包含blocker, critical, normal, minor, trivial几个不同的等级
    - 测试用例优先级1：blocker，中断缺陷（客户端程序无响应，无法执行下一步操作）
    - 测试用例优先级2：critical，临界缺陷（ 功能点缺失）
    - 测试用例优先级3：normal，普通缺陷（数值计算错误）
    - 测试用例优先级4：minor，次要缺陷（界面错误与UI需求不符）
    - 测试用例优先级5：trivial级别，轻微缺陷（必输项无提示，或者提示不规范）'
- @allure.feature("测试模块_demo1")
  - 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
- @allure.story("测试模块_demo2")
  - 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
- @allure.issue("BUG号：123")
  - 问题标识，关联标识已有的问题，可为一个url链接地址
- @allure.testcase("用例名：测试字符串相等")
  - 用例标识，关联标识用例，可为一个url链接地址

---

**整个框架主要分为三层，Base层、PageObject层、TestCase层，采用传统的互联网的垂直架构模式。**
**元素公共操作方法封装存放在Base层**
**页面元素操作存放在第二层PageObject层，后面如果页面元素变化，直接在第二层相应的Page对象修改即可**
**测试case存放在TestCases层，主要做断言等操作**

---

**安装所需要的包，使用pycharm导入项目，打开pycharm的terminal，只要到 requirements.txt 所在的目录下，使用如下命令 ，就能在当前的 python 环境中导入所有需要的包：**
`pip install -r requirements.txt`

---
**环境说明：**
**开发工具：pycharm**
**python版本：python3.8**
**测试case总入口：run.py**
**浏览器：Chrome**
**webdriver请选择对应Chrome版本的driver，并且放入python的安装目录中**

---

**有任何使用问题请联系我：chineseluo**

---

### 环境搭建

- python安装，`version:3.7`
- java环境配置，`version 1.8`，win10系统中配置配置java环境，参考[win10java环境配置](https://www.runoob.com/w3cnote/windows10-java-setup.html)
- allure安装：
  - 不同平台安装allure的方法不同，这里仅介绍windows平台下allure的安装步骤。其它平台请阅读[allure官方文档](https://docs.qameta.io/allure/)进行操作
  - 官方提供的安装方法可能会受网络环境影响而安装失败，可选择在[GitHub仓库](https://github.com/allure-framework/allure2 )下载文件并安装allure2
  - Windows环境下可以用以下步骤进行安装
    - 安装scoop，使用**管理员权限**打开powershell窗口，输入命令`Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')`
    - 如果安装不成功则运行`Set-ExecutionPolicy RemoteSigned -scope CurrentUser`，运行成功后重新执行第一步
    - scoop安装成功后控制台会输出`Scoop was installed successfully!`
    - 执行`scoop install allure`进行allure的安装
    - allure安装成功后控制台会输出`'allure' (2.13.1) was installed successfully!`

---

**selenium本地分布式启动配置：**
*1、配置JDK环境1.8，使用javac 检查java环境是否配置完成*
*2、下载selenium-server-standalone，下载地址：http://selenium-release.storage.googleapis.com/index.html，需要对应自己本地的selenium版本*
*3、下载对应的浏览器的driver，放置到python的安装目录(chrome：https://sites.google.com/a/chromium.org/chromedriver/downloads、firefox：https://github.com/mozilla/geckodriver/releases、ie：http://selenium-release.storage.googleapis.com/index.html?path=3.5/)*
*4、启动hub节点（管理节点负责任务的分发，数据收集统计）java -jar selenium-server-standalone-3.5.0.jar -role hub（ps:端口可以修改）*
*5、启动node节点java -jar selenium-server-standalone-3.5.0.jar -role node -port 5555 -hub http://localhost:4444/grid/register（ps:端口可以修改，需要启用多少个node节点，只需要修改port即可）*
*6、测试代码：test_mul_node.py，当三个浏览器都打开，说明环境配置没问题*



---

**本地启动分布式调试方法**

1、执行start_server.bat，启动hub与node，使用浏览器登录127.0.0.1:4444，点击console看到，三个node的节点信息，表示分布式服务启动成功

2、执行start_run_all_browser，启动三种浏览器执行脚本模式（IE需要进行浏览器设置，否则会执行失败）

---

**docker启动分布式调试方法**

一、拉取selenium的docker镜像

~~~ 镜像拉取
docker pull selenium/hub
docker pull selenium/node-firefox
docker pull selenium/node-chrome
~~~

二、检查镜像是否拉取成功

~~~ 检查镜像
docker images | grep selenium
~~~

三、启动docker镜像

~~~ 启动docker镜像
docker run -p 5555:4444 -d --name hub selenium/hub
docker run -P -d --link hub:hub --name firefox selenimu/node-firefox
docker run -P -d --link hub:hub --name chrome selenimu/node-chrome
~~~

四、检查是否启动成功

使用docker环境宿主机的IP+映射的端口进行访问，查看console，查看与hub节点建立连接的node节点的IP和端口等信息是否正确

五、调试模式（可选）

1、server+browser调试模式：使用服务端和node集成在一起的镜像

~~~ 镜像
docker pull selenium/standalone-chrome-debug
docker pull selenium/standalone-firefox-debug
~~~

2、server+node(browser)调试模式，使用hub+node的方式，镜像使用debug级别日志

~~~ 镜像
docker pull selenium/standalone-chrome-debug
docker pull selenium/standalone-firefox-debug
~~~

~~~ 建立容器链接
docker run -d -p 5900:5900 --link hub:hub selenium/node-chrome-debug
~~~

查看Linux下浏览器运行的图形界面

使用vnc viewer，下载地址：`https://www.realvnc.com/en/connect/download/viewer/windows/`

输入docker所在环境的宿主机IP+映射的端口（5900）进行连接，默认密码：secret

---

### 如何编写测试用例

下面详细说明如何添加一条用例，以登录界面演示

1、在PageObject模块创建一个login_page.py

![image-20200601211103002](C:\Users\chineseluo\AppData\Roaming\Typora\typora-user-images\image-20200601211103002.png)

2、封装login页面操作元素对象

~~~ login_page.py
# coding:utf-8
from Base.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver


# 封装速涡手游加速器登录页面操作对象及各个元素及操作方法
class Login_page(Base):
    def __init__(self, driver):
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
        return super().get_placeholder((By.NAME, "Username"))

    def get_password_attribute_value(self):
        """
            获得密码输入框的placeholder值
        @return:获得密码输入框的placeholder值
        """
        return super().get_placeholder((By.NAME, "Password"))
~~~



3、在TestCases下面新建一个包，例如Login模块，测试登录页面

![image-20200601210858042](C:\Users\chineseluo\AppData\Roaming\Typora\typora-user-images\image-20200601210858042.png)

4、在Login下面创建一个conftest.py和test_login_page_case.py

conftest.py中指定需要加载的测试页面对象，使用scope级别为function

~~~ conftest.py
import pytest
from PageObject.login_page import Login_page


@pytest.fixture(scope="function")
def login_page_class_load(function_driver):
    login_page = Login_page(function_driver)
    yield login_page
~~~

test_login_page_case.py中每个测试case需要调用页面模块conftest.py中的function，以及全局配置conftest.py中function_driver（或者function_remote_driver，分布式需要使用该参数)，断言使用Base模块中的assert_method的Assert_method，里面封装了断言方法，包含了allure断言失败截图等操作，根据不同的断言场景取用，或者自己再进行封装

~~~ test_login_page_case.py
# coding:utf-8
import pytest
import allure
import inspect
import logging
from Base.assert_method import Assert_method


@allure.feature("Login_page_case")
class Test_login_page_case:

    @allure.story("Login")
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.link("https://www.baidu.com", name="连接跳转百度")
    @allure.testcase("https://www.sina.com", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    def test_DLZC1(self, login_page_class_load, function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        login_page_class_load.login_by_config_url()
        username_input_attribute_value = login_page_class_load.get_username_attribute_value()
        Assert_method.assert_equal_screen_shot(function_driver, (username_input_attribute_value, "手机号码"))
~~~

5、执行用例

执行用例可以通过两种常用的方法进行

1. pycharm中配置`test runner`为`pytest`，配置路径为`settings->Tools->Python Integrated Tools->Testing`；配置完成后就能够在打开测试用例文件后看到可执行的按钮了
2. 在根目录下的`run.py`文件中运行，需要配置要运行的`Fixture`后就可以运行了。例如当你在调试`Login`时只需要保证`allure_features_list`中只有`Login`就行了，`pytest`会自动寻找`Fixture`值为`Login`参数的用例

![image-20200601211933915](C:\Users\chineseluo\AppData\Roaming\Typora\typora-user-images\image-20200601211933915.png)