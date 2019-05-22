#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/6 19:59 
# @Author : Zero 
# @Site :  
# @File : operateYaml.py 
# @Software: PyCharm
import yaml
from common import test_class as o
'''
读取文件信息
'''
def getYam(homeyaml):
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            return x
    except FileNotFoundError:
        print("文件没找到")
'''
获取元素公共id，查找到元素库内容
'''
# def getElement(homeyaml):
#     x = getYam(homeyaml)
# x = getYam("../img/element.yaml")
# print(x)
# def add(a, b):
#     d = {
#     "a" : lambda : a+b ,
#     'b': 456
#     }
#     return d['a']()
# print(add(1,2))
getYam("C://Users//17673//PycharmProjects//Appnium//testCase//yaml//login//home_login.yaml")