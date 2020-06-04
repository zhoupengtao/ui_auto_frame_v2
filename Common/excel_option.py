# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
import xlrd
import xlwt


# 封装操作excel的方法
class Excel_option:
    def read_excel(self,file_name, index):
        """

        @param file_name: 文件名
        @param index: 索引
        @return: 字典
        """
        test_data_path = file_name
        xls = xlrd.open_workbook(test_data_path)
        sheet = xls.sheet_by_index(index)
        data_dir = {}
        for i in range(sheet.ncols):
            data = []
            for j in range(sheet.nrows):
                if j == 0:
                    continue
                else:
                    data.append(sheet.row_values(j)[i])
            data_dir[i] = data
        return data_dir
