#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/7/8 19:15 
# @Author : Zero 
# @Site :  
# @File : test.py 
# @Software: PyCharm
from appium import webdriver
from common import operateElement as bo
import time

desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '7.0',
        'appPackage': 'com.unovo.apartment.manager.dev',
        'appActivity': 'com.lianyuplus.login.ui.StartActivity'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
go = bo.OperateElement(driver)
go.operate_swipe_left()
print(0)
print(1)
print(1)
print(1)
print(1)
