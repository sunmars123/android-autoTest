#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/11 15:06 
# @Author : Zero 
# @Site :  
# @File : server.py 
# @Software: PyCharm
'''
testDAL下server的实现类
'''
from testDAL import server
class AppniumServer():
    def __init__(self, l_devices):
        '''
        appnium服务启动对象赋值
        :param l_devices: appnium启动信息自带你
        '''
        self.server = server.AppniumServer(l_devices)
    def start_server(self):
        '''
        启动appnium服务
        :return: 无返回
        '''
        self.server.start_server()
    def stop_server(self):
        '''
        停止appnium服务
        :return: 无返回
        '''
        self.server.stop_server()
    def is_runnnig(self):
        '''
        判断appnium服务是否已经运行
        :return: 返回判断结果(True，False)
        '''
        return self.server.is_runnnig()