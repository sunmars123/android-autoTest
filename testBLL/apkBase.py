#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/7 17:12 
# @Author : Zero 
# @Site :  
# @File : apkBase.py 
# @Software: PyCharm
'''
testDAL下apkBase的实现类，用于获取信息
'''
from testDAL import apkBase
class apkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath
        self.appinfo = apkBase.ApkInfo(self.apkpath)
    def get_apk_name(self):
        '''
        获取apk的名称
        :return: apk名称
        '''
        return self.appinfo.get_apk_name()
    def get_apk_pkg(self):
        '''
        获取启动app的包名
        :return:app包名
        '''
        return self.appinfo.get_apk_pkg()
    def get_apk_activity(self):
        '''
        获取app的activity
        :return:activity
        '''
        return self.appinfo.get_apk_activity()
    def clearApp(self):
        return self.appinfo.clearApp()