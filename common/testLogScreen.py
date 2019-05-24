#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/13 15:40 
# @Author : Zero 
# @Site :  
# @File : testLogScreen.py 
# @Software: PyCharm
import time

def screenshotNG(caseName, driver, resultPath):
    '''
    错误截图
    :param caseName:测试类名称
    :param driver:驱动对象
    :param resultPath:截图保存路径
    :return:图片信息
    '''
    logPath = time.strftime('%Y%m%d%H%M%S', time.localtime())
    screenshotName = "CheckPoint_NG.png"
    screen_img = resultPath+caseName+"_"+logPath +"_"+screenshotName
    driver.get_screenshot_as_file(screen_img)
    return screen_img