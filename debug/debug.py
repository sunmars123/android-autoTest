#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/17 18:10 
# @Author : Zero 
# @Site :  
# @File : debug.py 
# @Software: PyCharm

# from appium import webdriver
# from testDAL import apkBase
# from common.variable import GetVariable as common
# import time
# import xlsxwriter
# x = apkBase.ApkInfo(common.APKPATH)
# print(x.get_apk_activity())
# print(x.get_apk_pkg())
# desired_caps = {
#         'platformName': 'Android',
#         'deviceName': '127.0.0.1:62001',
#         'platformVersion': '7.0',
#         'appPackage': 'com.unovo.apartment.v2.dev',
#         'appActivity': 'com.unovo.plugin.account.SplashActivity'
#     }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# time.sleep(5)
# driver.find_element_by_id("com.unovo.apartment.v2.dev:id/editMobile").send_keys("17673637740")
# x = driver.find_element_by_id("com.unovo.apartment.v2.dev:id/editMobile")
# print(x.text)
# print(x.get_attribute())
# # # driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys("17673637740")
# # # driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys("Ct123456")
# # driver.find_element_by_id('com.unovo.apartment.manager.dev:id/btnLogin').click()
# 创建excel
# workbook = xlsxwriter.Workbook("weather.xlsx")
# # 创建sheet & 命名
# worksheet = workbook.add_worksheet("test")
# # 设置行高
# worksheet.set_row(1, 100)
# worksheet.set_row(2, 100)
# # 设置格式
# a = workbook.add_format({'align': 'center','valign': 'vcenter','border':1, 'bold':True, 'text_wrap':True})
# # 写入单元格内容并插入格式
# worksheet.write("A1", "姓名11111111111111111111111111111111111", a)
from testMode import appCase as m_app_case
from testBLL import appCase as b_app_case
bc = b_app_case.GetAppCase(test_module="登录", GetAppCaseInfo=m_app_case.GetAppCaseInfo, GetAppCase=m_app_case.GetAppCase)
bc.execCase("../testCase/yaml/bys/login/test.yaml")
print(1)