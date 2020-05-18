#UI_auto_project框架解释
#Base模块封装操作元素的公共方法
#Common模块是封装的读取配置文件的公共方法，类似于util工具类
#Data模块，用于存放数据驱动源数据
#Logs模块，用于生成日志文件
#PageObject模块提取页面对象封装公共操作方法
#Reports模块，存放测试报告，以及测试报告的生成模板HTMLTestRunner.py
#TestCases模块，用于存放测试case


#整个框架主要分为三层，Base层、PageObject层、TestCase层，采用传统的互联网的垂直架构模式。
#元素公共操作方法封装存放在Base层
#页面元素操作存放在第二层PageObject层，后面如果页面元素变化，直接在第二层相应的Page对象修改即可
#测试case存放在TestCases层，主要做断言等操作


#安装所需要的包，使用pycharm导入项目，打开pycharm的terminal，只要到 requirements.txt 所在的目录下，使用如下命令 ，就能在当前的 python 环境中导入所有需要的包：
#pip install -r requirements.txt

#环境说明：
#开发工具：pycharm
#python版本：python3.8
#测试case总入口：suite.py
#浏览器：Chrome
#webdriver请选择对应Chrome版本的driver，并且放入python的安装目录中

#联系人：成都-阿木木
#邮箱：848257135@qq.com
#有任何使用问题请联系我


