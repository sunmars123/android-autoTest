#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/8 10:23 
# @Author : Zero 
# @Site :  
# @File : testUnittest.py
# @Software: PyCharmbuyu
from testMode import appCase
from testDAL import appCase
# l = [{"a":123}, {"test_id":456}]
# d = appCase.AppCase(GetAppCaseInfo=appCase.AppCase)
#
# d.GetAppCaseInfo.test_id = l[1].get("test_id","false")
d = {'element_id': 1, 'element_info': 'android.widget.EditText', 'find_type': 'class_names', 'index': 0.0, 'enable': 0.0}
x = {'element_info': 'false', 'element_id': 1, 'enable': 'false', 'operate_type': 'send_keys', 'msg': None, 'find_type': 'false', 'time': 0, 'name': None, 'index': 'false', 'data_input': 17673637740, 'log': None}
x.update(d)