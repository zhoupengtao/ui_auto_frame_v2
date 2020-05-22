# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 11:02
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : ohter_test_code.py
# @Software: PyCharm

import os
import json
json_data = '{"login":[{"username":"aa","password":"001"},{"username":"bb","password":"002"}],"register":[{"username":"cc","password":"003"},{"username":"dd","password":"004"}]}'
with open('../Report/allure-results/widgets/environment.json', 'w', encoding='utf-8') as fw:
    try:
        print("开始创建文件")
        json.dump(json.loads(json_data), fw, ensure_ascii=False, indent=4)
        #f.close()
        print("文件创建结束：{}".format(fw))
    except Exception as e:
        print("文件生成失败{}".format(e))
    print(type(json.loads(json_data)))
