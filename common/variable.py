#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/6 19:10 
# @Author : Zero 
# @Site :  
# @File : variable.py 
# @Software: PyCharm
'''
配置信息
'''
class GetVariable(object):
    # 元素定位类型
    NAME = "name"
    ID = "id"
    XPATH = "xpath"
    INDEX = "index"
    find_element_by_id = "by_id"
    find_elements_by_id = "by_ids"
    find_element_by_name = "by_name"
    find_elements_by_name = "by_names"
    find_element_by_link_text ="by_link_text"
    find_elements_by_link_text = "by_link_texts"
    find_element_by_xpath = "by_xpath"
    find_elements_by_xpath = "by_xpaths"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
    # 自动化类型
    SELENIUM = "selenium"
    APPIUM = "appium"
    SELENIUM_APPIUM = "appium"
    # 系统版本
    ANDROID = "android"
    IOS = "ios"
    IE = "ie"
    # 浏览器版本
    FOXFIRE = "foxfire"
    CHROME = "chrome"


    #操作类型
    CLICK = "click"
    SEND_KEYS = "send_keys"
    SEND_CODE = "send_code" # 输入验证码
    SWIPELEFT = "swipeLeft"


    DRIVER = ""
    TAP = "tap"

    FIND_STR = "find_str"
    WAIT_TIME = 10

    # 配置文件地址
    COMMONELEMENT = "../img/demo.xlsx"
    APKPATH = "../img/lianyuplus-baiyunshen-3.2.0-beta-release-build2019051701.apk"
    # 报告输出地址
    REPORT_INFO_PATH = "../../../Logs/info.txt"
    REPORT_INIT = "F:/init.txt"
    REPORT_COLLECT_PATH = "../../../Logs/collect.txt"
    SCREEN_IMG_PATH = "../../../report/failImg/" # 截图地址