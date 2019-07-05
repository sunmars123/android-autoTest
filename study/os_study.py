#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/4 17:32 
# @Author : Zero 
# @Site :  
# @File : os_study.py 
# @Software: PyCharm
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
# 拼接路径并返回文件绝对路径
print(PATH(""))
# 返回当前路径
print(os.path.dirname(__file__))