#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/7 19:16 
# @Author : Zero 
# @Site :  
# @File : appCase.py 
# @Software: PyCharm
'''
testDAL下AppCase的实现类
'''
from testDAL import appCase
class GetAppCase():

    def __init__(self, **kwargs):
        '''
        初始化构造得到testDAL对象执行用例
        :param kwargs:
        test_module:'模块名'
        GetAppCaseInfo: '用例详情' model层
        GetAppCase: 'app case' model层
        package： 包名
        devices: 设备名
        '''
        self.kwargs = kwargs
        self.be = appCase.AppCase(**self.kwargs)
    def execCase(self, f, **kwargs):
        '''
        用例执行函数
        :param f:
        :param kwargs:
        :param kwargs:
        test_name: 用例名
        is_last: 最后一个用例 1, 0
        :return:
        '''
        self.be.execCase(f, **kwargs)
    # def report(self, go, ch_check, _d_report_common, kwargs):
    #     self.be.report(go, ch_check, _)