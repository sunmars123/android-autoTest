#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/11 15:06 
# @Author : Zero 
# @Site :  
# @File : server.py 
# @Software: PyCharm
import threading
import os
import urllib.request
from multiprocessing import Process
from urllib.error import URLError
from common import logger
testLog = logger.Logger("../../../Logs/all.log", level="debug")
class AppniumServer:
    def __init__(self, l_devices):
        self.l_devices = l_devices
    '''
    启动appium服务
    '''
    def start_server(self):
        '''
        start the appnium server
        :return:
        '''
        for i in range(0, len(self.l_devices['appium'])):
            t1 = RunServer(self.l_devices['appium'][i]['config'])
            p = Process(target=t1.start())
            p.start()
        testLog.logger.debug("启动appium服务")
    def stop_server(self):
        """stop the appium server
        selenium_appium: appium selenium
        :return:
        """
        os.system('taskkill /f /im  node.exe')
        testLog.logger.debug("停止appium服务")
    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        for i in range(0, len(self.l_devices["appium"])):
            url = " http://127.0.0.1:"+str(self.l_devices["appium"][i]["port"])+"/wd/hub"+"/status"
            print(url)
            try:
                response = urllib.request.urlopen(url, timeout=5)

                if str(response.getcode()).startswith("2"):
                    return True
                else:
                    return False
            except URLError:
                return False
            finally:
                if response:
                    response.close()

class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        x = "%s" % self.cmd
        os.system("%s" % self.cmd)


