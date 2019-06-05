#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/7 17:04 
# @Author : Zero 
# @Site :  
# @File : apkBase.py 
# @Software: PyCharm
import os
import re
import sys
from common import logger
testLog = logger.Logger("../../../Logs/all.log")
'''
获取app信息模块工具类，功能：得到应用名称、得到包名、得到启动类名
'''
import subprocess
class ApkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath

    #得到应用名字
    def get_apk_name(self):
        testLog.logger.debug("run function ==> %s"% sys._getframe().f_code.co_name)
        cmd = "aapt dump badging " + self.apkpath + " | grep application-label: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[0].decode()[18:]
        return result

    # 得到包名
    def get_apk_pkg(self):
        testLog.logger.debug("run function ==> %s" % sys._getframe().f_code.co_name)
        cmd = "aapt dump badging %s" % self.apkpath
        results = os.popen(cmd, 'r')
        a = ""
        while 1:
            line = results.readline()
            if not line: break
            a += line
        results.close()
        result1 = re.findall(".*package: name='(.+?)' versionCode='.*", a)
        return result1[0]

    #得到启动类
    def get_apk_activity(self):
        testLog.logger.debug("run function ==> %s" % sys._getframe().f_code.co_name)
        cmd = "aapt dump badging %s" % self.apkpath
        results = os.popen(cmd, 'r')
        a = ""
        print(results)
        while 1:
            line = results.readline()
            if not line: break
            a += line
        results.close()
        result1 = re.findall(".*launchable-activity: name='(.+?)'  label='' icon=''.*", a)
        return result1[0]
# if __name__ == '__main__':
#     ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_pkg()
#     # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_version()
#     # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_name()
#     ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()
#     # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()