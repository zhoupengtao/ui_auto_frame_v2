::批量启动selenium-server-standalone服务
@echo off
start  /D "Grid_server/selenium_server" selenium_server_hub.bat
start  /D "Grid_server/selenium_server" selenium_server_node1.bat
start  /D "Grid_server/selenium_server" selenium_server_node2.bat
start  /D "Grid_server/selenium_server" selenium_server_node3.bat