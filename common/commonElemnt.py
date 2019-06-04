#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/1 15:39 
# @Author : Zero 
# @Site :  
# @File : commonElemnt.py
# @Software: PyCharm

import xlrd
import xlwt
from datetime import date, datetime

class Element:
    def __init__(self, f):
        self.f = f
        self.workbook = xlrd.open_workbook(f)
    '''
    获取元素编号字典
    '''
    def getElement(self, sheetName="Sheet1"):
        sheet = self.workbook.sheet_by_name(sheetName)
        dic = {}
        rows = sheet.nrows
        for i in range(rows):
            row = sheet.row_values(i)
            dic_value = {}
            if i!= 0:
                dic_value ["element_id"] = row[5]
                dic_value ["element_info"] = row[6]
                dic_value ["find_type"] = row[7]
                dic_value ["index"] = int(row[8])
                dic_value ["enable"] = int(row[9])
                dic[row[5]] = dic_value
        return dic
    '''
    判断用例元素的元素编号是否存在元素库
    '''
    def isElemnet(self, id):
        dic = self.getElement()
        if id in dic.keys():
            return True
        return False
    '''
    拼接用例元素和公用元素内容
    '''
    def joinElement(self, bc, id):
        dic = self.getElement()
        bc.update(dic[id])
        return bc