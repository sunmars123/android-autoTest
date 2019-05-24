#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/23 15:28 
# @Author : Zero 
# @Site :  
# @File : logNameFormat.py
# @Software: PyCharm
import time
def infoLog():
    logPath = time.strftime('%Y%m%d%H%M%S', time.localtime())
    infoName = "info.txt"
    info = infoName+"_"+logPath
    return info

def collectLog():
    logPath = time.strftime('%Y%m%d%H%M%S', time.localtime())
    collectName = "info.txt"
    collect = collectName+"_"+logPath
    return collect
