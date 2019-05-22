#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/11 16:20 
# @Author : Zero 
# @Site :  
# @File : login.py 
# @Software: PyCharm
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import appCase as b_app_case
from testMode import appCase as m_app_case
from testRunner.runnerBase import TestInterfaceCase as te
from testBLL import apkBase
import time
class testLogin2(te):

    def setUp(self):
        super(testLogin2, self).setUp()
        time.sleep(10)
        self.bc = b_app_case.GetAppCase(test_module="我的", GetAppCaseInfo=m_app_case.GetAppCaseInfo, GetAppCase=m_app_case.GetAppCase,
                                        driver=self.driver)
    # def home_feed(self):
    #     self.bc.execCase(PATH("yaml/myinfo/home_feed.yaml"), test_name="test_home_feed", isLast="1")

    # 单点登陆这里特殊处理,不同的设备调用不同的case
    def home_login(self):
        home_logon_yaml = PATH("yaml/login/home_login2.yaml")
        self.bc.execCase(home_logon_yaml, test_name="test_home_login2", test_module="我的")
    def home_login2(self):
        home_logon_yaml = PATH("yaml/login/home_login3.yaml")
        self.bc.execCase(home_logon_yaml, test_name="test_home_login2", test_module="我的")
    # def get_apk_pkg(self):
    #     return apkBase.apkInfo(PATH("../img/com.unovo.apartment.manager.dev.apk")).get_apk_pkg()

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
        # self.home_feed()
    def test_home2(self):
        # self.home_fist_open()
        self.home_login2()
        # self.home_feed()