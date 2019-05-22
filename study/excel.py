#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/2 16:17 
# @Author : Zero 
# @Site :  
# @File : excel.py 
# @Software: PyCharm

import xlsxwriter

# 创建excel
workbook = xlsxwriter.Workbook("weather.xlsx")
# 创建sheet & 命名
worksheet = workbook.add_worksheet("test")
'''
格式设置
'''
# 设置行高
worksheet.set_row(1, 100)
worksheet.set_row(2, 100)
# 设置格式
a = workbook.add_format({'align': 'center','valign': 'vcenter','border':1, 'bold':True, 'bg_color':"blue", 'color':'#ffffff'})
a2 = workbook.add_format({'align': 'center','valign': 'vcenter','border':1, 'bold':True})
# 写入单元格内容并插入格式
worksheet.write("A1", "姓名", a)
worksheet.write("A5", "", a2)
# 合并单元格并格式化输出
worksheet.merge_range("A2:B2", "陈涛", a)
workbook.close()