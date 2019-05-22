#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/11 13:42 
# @Author : Zero 
# @Site :  
# @File : adbCommon.py 
# @Software: PyCharm
from testDAL import adbCommon
'''
testDAL模块的实现引用，查看设备是否存在
'''
def attached_devices():
    return adbCommon.AndroidDebugBridge().attached_devices()