#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/11 16:20 
# @Author : Zero 
# @Site :  
# @File : login.py 
# @Software: PyCharm
import os
'''
p匿名函数，拼接路径并返回用例的绝对路径'\'
'''
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import appCase as b_app_case
from testMode import appCase as m_app_case
from testRunner.runnerBase import TestInterfaceCase as te
# from testBLL import apkBase
import time
class testLogin1(te):
    # 测试前需要执行得操作
    def setUp(self):
        super(testLogin1, self).setUp()
        time.sleep(2)
        self.bc = b_app_case.GetAppCase(test_module="我的", GetAppCaseInfo=m_app_case.GetAppCaseInfo, GetAppCase=m_app_case.GetAppCase,
                                        driver=self.driver, devices=self.l_devices["deviceName"])
    # def home_feed(self):
    #     self.bc.execCase(PATH("yaml/myinfo/home_feed.yaml"), test_name="test_home_feed", isLast="1")

    # 单点登陆这里特殊处理,不同的设备调用不同的case
    def home_login(self):
        home_logon_yaml = PATH("yaml/login/home_login.yaml")
        # if self.l_devices["deviceName"] == "GWY0217113000393":
        #     home_logon_yaml = PATH("yaml/login/home_login.yaml")
        # if self.l_devices["deviceName"] == "MSM8926":
        #     home_logon_yaml = PATH("yaml/myinfo/home_login1.yaml")
        x = self.bc.execCase(home_logon_yaml, test_name="test_home_login", isLast="0", test_module='我的')
        self.assertTrue(x)
    # def get_apk_pkg(self):
    #     return apkBase.apkInfo(PATH("../img/com.unovo.apartment.manager.dev.apk")).get_apk_pkg()

    # 测试用例执行完后所需执行的操作
    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass
    @staticmethod
    def tearDownClass():
        pass
    def test_home(self):
        # self.home_fist_open()
        self.home_login()