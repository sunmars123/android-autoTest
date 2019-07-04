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
            x = yaml.load(f, Loader=yaml.FullLoader)
            return x
    except FileNotFoundError:
        print("文件没找到")
'''
获取元素公共id，查找到元素库内容
'''