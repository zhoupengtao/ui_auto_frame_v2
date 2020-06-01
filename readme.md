### ui_auto_frame框架解释:使用pytest+selenium+allure

---

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

**有任何使用问题请联系我**

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