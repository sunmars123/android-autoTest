#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/6 19:11 
# @Author : Zero 
# @Site :  
# @File : dataToString.py 
# @Software: PyCharm
"""
时间格式化输入函数
"""
import time
'''
根据传入得时间和格式，返回时间
t_time:时间time.localtime()
format:格式,如%Y-%m-%d %H:%M %p
'''
def getStrTime(t_time, format):
    # 根据出入的格式输出时间
    return time.strftime(format, t_time)
