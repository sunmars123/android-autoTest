#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/7 17:02 
# @Author : Zero 
# @Site :  
# @File : runnerBase.py 
# @Software: PyCharm
from common.variable import GetVariable as common
from appium import webdriver
from testBLL import apkBase
import unittest

'''
提供一个获取driver对象的函数
'''
def appnium_testcase(l_devices):
    apk_base = apkBase.apkInfo("../img/com.unovo.apartment.manager.dev.apk")
    derired_caps = {}
    derired_caps['platformName'] = l_devices['platformName']
    derired_caps['platformVersion'] = l_devices['platformVersion']
    derired_caps['appPackage'] = l_devices['appPackage']
    derired_caps['appActivity'] = l_devices['appActivity']
    derired_caps['deviceName'] = l_devices['deviceName']
    remote = "http://127.0.0.1:4723/wd/hub"
    driver = webdriver.Remote(remote, derired_caps)
    return driver

'''
定义测试类 继承TestCase
'''
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest', l_devices=None):
        super(TestInterfaceCase, self).__init__(methodName)
        self.l_devices = l_devices
        # self.driver = ""
    '''
    运行每个测试用例前启动driver
    '''
    def setUp(self):
        if self.l_devices["platformName"] == common.ANDROID:
            self.driver = appnium_testcase(self.l_devices)
    '''
    运行每个测试用例后关闭driver
    '''
    def tearDown(self):
        self.driver.close_app()
    '''
    运行完成当前测试模块后运行
    '''
    @staticmethod
    def tearDownClass():
        # driver.close_app()
        # driver.quit()
        print('tearDownClass')
    @staticmethod
    def parametrize(testcase_klass, l_devices=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, l_devices=l_devices[0]))
        return suite
