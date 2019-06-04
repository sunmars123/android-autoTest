#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/11 13:30 
# @Author : Zero 
# @Site :  
# @File : runner.py 
# @Software: PyCharm
import xlsxwriter
import sys
sys.path.append("..")
from common import operateYaml, dataToString
from testBLL import adbCommon
from testBLL import server
import time
from multiprocessing import Pool
import datetime
import unittest
from testCase.login import testLogin
from testRunner.runnerBase import TestInterfaceCase
from common import OperateFile
from common.variable import GetVariable as common
from testBLL import report as b_report
from testDAL import HTMLTestRunner
import sys
import os
from common import logger
# 增加cmd执行路径引导
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
testLog = logger.Logger("../../../Logs/all.log")
'''
获取driver信息
'''
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def get_devices():
    return operateYaml.getYam("../devices.yaml")
ga = get_devices()

data = {"init":[], "info":[]}
'''
读取报告
'''
def read_report(f=""):
    op = OperateFile.OperateFile(f, "r")
    return op.read_txt_row()
# 得到总统计的case
def get_report_collect(start_test_time, endtime, starttime):
    _read_collect_json = eval(read_report(common.REPORT_COLLECT_PATH))
    for key in _read_collect_json:
        data[key] = _read_collect_json[key]
    data["app_name"] = "联寓运营ＦＷ"
    data["test_sum_date"] = str((endtime - starttime).seconds) + "秒"
    data["test_date"] = start_test_time
    data["app_size"] = "0M"
    data["app_version"] = "1.0"
def get_report_info():
    data["info"] = eval(read_report(common.REPORT_INFO_PATH))["info"]
def get_common_report(start_test_time, endtime, starttime):
    get_report_collect(start_test_time, endtime, starttime)
    get_report_info()
'''
运行用例池
'''
def runnerPool():
    devices_Pool = []
    for i in range(0, len(ga["appium"])):
        l_pool = []
        t = {}
        t["deviceName"] = ga["appium"][i]["devices"]
        t["platformVersion"] = ga['appium'][i]['platformVersion']
        t["platformName"] = ga["appium"][i]["platformName"]
        t["port"] = ga["appium"][i]["port"]
        t['appPackage'] = ga['appium'][i]['appPackage']
        t['appActivity'] = ga['appium'][i]['appActivity']
        l_pool.append(t)
        devices_Pool.append(l_pool)
        testLog.logger.info("获取驱动启动信息")
    pool = Pool(len(devices_Pool))
    # for i in range(2):
    #     pool.apply_async(sample_request, args=(t[i],)) # 异步
    testLog.logger.info("开始执行测试线程")
    pool.map(runnerCaseApp, devices_Pool)
    testLog.logger.info("测试线程执行完成")
    pool.close()
    testLog.logger.info("测试完成，线程结束")
    pool.join()

'''
运行测试用例
'''
def runnerCaseApp(l_devices):
    start_test_time = dataToString.getStrTime(time.localtime(), "%Y-%m-%d %H:%M %p")
    starttime = datetime.datetime.now()
    suite = unittest.TestSuite()
    # suite.addTest(TestInterfaceCase.parametrize(testLogin1, l_devices=l_devices))
    testLog.logger.info("开始加载用例")
    suite.addTest(TestInterfaceCase.parametrize(testLogin, l_devices=l_devices))
    # suite.addTest(testLogin1.home_login())
    # suite.addTest(testLogin2.home_login())
    testLog.logger.info("用例加载完成")
    fp = open("../../../report/res.html", "wb")
    testLog.logger.info("开始运行用例池")
    HTMLTestRunner.HTMLTestRunner(stream=fp, title='all_tests', description='所有测试情况').run(suite)
    testLog.logger.info("用例运行完成，准备输出报告")
    endtime = datetime.datetime.now()
    get_common_report(start_test_time, endtime, starttime)
    report()
def report():
    workbook = xlsxwriter.Workbook('../../../report/GetReport.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    print(data)
    b_OperateReport = b_report.OperateReport(wd=workbook, data=data)
    b_OperateReport.init(worksheet)
    b_OperateReport.detail(worksheet2)
    b_OperateReport.close()
'''
函数主方法
'''
if __name__ == '__main__':
    testLog.logger.info("获取驱动信息")
    if adbCommon.attached_devices():
        appium_server = server.AppniumServer(ga)
        appium_server.stop_server()
        appium_server.start_server()
        testLog.logger.info("启动appium服务")
        while not appium_server.is_runnnig():
            time.sleep(2)
        runnerPool()
        appium_server.stop_server()
        testLog.logger.info("停止appium服务")
    else:
        testLog.logger.warning("设备不存在")