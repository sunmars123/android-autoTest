#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/8 10:55 
# @Author : Zero 
# @Site :  
# @File : appCase.py 
# @Software: PyCharm
from schematics.models import Model
from schematics.types import StringType,IntType
'''
用例的操作
'''
class GetAppCase(Model):
    element_info = StringType() # (查找类型：name/id/xpah)
    element_id = IntType()
    enable = IntType()
    operate_type = StringType() #具体的详情,如xpath:“/android.widget.TextView[contains(@text,'Add note'")）,id等
    msg = StringType() # 输入的内容
    find_type = StringType() # 操作类型。比如点击，下拉，拖动等等，对应common
    time = IntType() # 配合与滑动操作
    name = StringType()
    index = IntType()
    data_input = StringType()# 输入信息
    log = StringType() # 本地log信息路径，一般由手机名字_型号构成
    ch_check = StringType() #检查点信息
'''
用例的基本信息
'''
class GetAppCaseInfo(Model):
    test_no = StringType() # 用例的id
    test_describe = StringType() # 用例的介绍
    test_name = StringType() # 用例的名字
    test_result =StringType() # 用例的结果
    test_reason = StringType() # 用例失败的理由
    test_module = StringType() # 测试的模板
    test_image = StringType() # 图片
    test_log = StringType() #闪退的日志
