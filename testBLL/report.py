#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/2 15:21 
# @Author : Zero 
# @Site :  
# @File : report.py 
# @Software: PyCharm
'''
testDAL下report的实现类
'''
from testDAL import report
class OperateReport:
    def __init__(self, wd=None, data=None):
        '''
        变量复制，得到excel操作对象、插入数据
        :param wd: Workbook对象
        :param data: 用例执行详情字典
        '''
        self.wd = wd
        self.data = data
        self.sr = report.OperateReport(self.wd, self.data)
    def init(self, worksheet):
        '''
        创建测试总况sheet，格式化键入内容
        :param worksheet:测试总况worksheet对象
        :return:无返回
        '''
        self.sr.init(worksheet)
    def detail(self, worksheet):
        '''
        创建测试详情sheet，格式化键入内容
        :param worksheet: 测试详情wordksheet对象
        :return: 无返回
        '''
        self.sr.test_detail(worksheet)
    def close(self):
        '''
        关闭操作流
        :return:
        '''
        self.sr.close()
    # def set_report(self, mreport):
    #     self.sr.set_report(mreport)