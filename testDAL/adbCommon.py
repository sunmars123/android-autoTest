#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/11 13:44 
# @Author : Zero 
# @Site :  
# @File : adbCommon.py 
# @Software: PyCharm
import os
class AndroidDebugBridge(object):
    '''
    打开设备
    '''
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, 'r')
        while 1:
            line = results.readline()
            if not line:break
            command_result += line
        results.close()
        return command_result
    # 检查设备
    def attached_devices(self):
        result = self.call_adb("devices")
        print(result)
        #获取到list中的driver信息
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        #判断是否存在设备
        flag = [device for device in devices if len(devices) >1 ]
        if flag:
            return True
        else:
            return False