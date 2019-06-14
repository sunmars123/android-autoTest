#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/17 18:10 
# @Author : Zero 
# @Site :  
# @File : debug.py 
# @Software: PyCharm

from appium import webdriver
from testDAL import apkBase
import time
from common.variable import GetVariable as common
x = apkBase.ApkInfo(common.APKPATH)
print(x.get_apk_activity())
print(x.get_apk_pkg())
desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '7.0',
        'appPackage': 'com.unovo.apartment.v2.dev',
        'appActivity': 'com.unovo.plugin.account.SplashActivity'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
# time.sleep(10)
# driver.find_element_by_id("com.unovo.apartment.manager.dev:id/login_tvForget").click()
# # driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys("17673637740")
# # driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys("Ct123456")
# driver.find_element_by_id('com.unovo.apartment.manager.dev:id/btnLogin').click()