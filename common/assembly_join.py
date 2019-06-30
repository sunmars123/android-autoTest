#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/28 14:22 
# @Author : Zero 
# @Site :  
# @File : assembly_join.py 
# @Software: PyCharm
from common import operateYaml
def get_assembly(assemblyPath):
    gh = operateYaml.getYam(assemblyPath)
    print(gh)
