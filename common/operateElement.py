#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/6 19:20 
# @Author : Zero 
# @Site :  
# @File : operateElement.py 
# @Software: PyCharm
'''
此脚本主要用于查找元素是否存在，操作页面元素
'''

from selenium.webdriver.support.ui import WebDriverWait as wait
from common.variable import GetVariable as common
import selenium.common.exceptions
import time
class OperateElement():

    def __init__(self, driver):
        '''

        :param driver: 初始化驱动类
        '''
        self.driver = driver
    def findElement(self, mOperate):
        '''
        查找元素
        :param mOperate: 用例某操作字典
        :return: 返回查找结果true、false
        '''
        try:
            # 设置等待超时，未找到元素设置重试
            wait(self.driver, common.WAIT_TIME).until(lambda x: elements_by(mOperate, self.driver))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            print("找不到数据")
        except IndexError:
            print("页面未加载出来")
    '''
    通过findElement方法判断操作类型并通过操作类型字典匹配操作方法执行操作
    '''
    def opearate_element(self, mOperate):
        '''

        :param mOperate: 用例操作字典
        :return: 根据匹配的值执行操作
        '''
        if self.findElement(mOperate):
            elements = {
                common.CLICK : lambda :opearte_click(mOperate, self.driver),
                common.SEND_CODE : lambda  :send_code(),
                common.SEND_KEYS : lambda  :send_keys(mOperate, self.driver),
                common.SWIPELEFT : lambda  :operate_swipe_left(mOperate, self.driver),
            }
            return elements[mOperate["operate_type"]]()
        return True

def elements_by(mOperate, cts):
    # print(len(cts.find_elements_by_class_name(mOperate['element_info'])[mOperate['index']]))
    # print(mOperate['index'])
    '''

    :param mOperate: 用例操作字典
    :param cts: driver对象
    :return: 页面定位元素对象
    '''
    try:
        if mOperate["find_type"] == common.find_elements_by_id:
            return cts.find_elements_by_id(mOperate["element_info"])
        elif mOperate["find_type"] == common.find_elements_by_name:
            return cts.find_elements_by_name(mOperate['name'])[mOperate['index']]
        elif mOperate["find_type"] == common.find_elements_by_class_name:
            return cts.find_elements_by_class_name(mOperate['element_info'])[mOperate['index']]
    except IndexError:
        print("找不到元素")
        return None
    elements = {
        common.find_element_by_id : lambda :cts.find_element_by_id(mOperate["element_info"]),
        # common.find_elements_by_id : lambda :cts.find_elements_by_id(mOperate["element_info"]),
        common.find_element_by_xpath: lambda :cts.find_element_by_xpath(mOperate["element_info"]),
        common.find_element_by_name: lambda :cts.find_element_by_name(mOperate['name']),
        # common.find_elements_by_name: lambda :cts.find_elements_by_name(mOperate['name'])[mOperate['index']],
        common.find_element_by_class_name: lambda :cts.find_element_by_class_name(mOperate['element_info']),
        # common.find_elements_by_class_name: lambda :cts.find_elements_by_class_name(mOperate['element_info'])[mOperate['index']]
    }
    return elements[mOperate["find_type"]]()
'''
通过字典的定位类型执行操作
'''
def opearte_click(mOperate, cts):
    '''

    :param mOperate: 用例操作字典
    :param cts: driver对象
    :return: 执行操作
    '''
    if mOperate["find_type"] == common.find_element_by_id or mOperate["find_type"] == common.find_element_by_xpath or mOperate["find_type"] == common.find_element_by_name:
        elements_by(mOperate, cts).click()
'''
左滑操作 暂未开发
'''
def operate_swipe_left(mOperate, cts):
    time.sleep(1)


'''
通过字典的定位类型执行输入操作，值提取字典钟的text文本
'''
def send_keys(mOperate, cts):
    '''

    :param mOperate: 用例操作字典
    :param cts: driver对象
    :return: 执行操作
    '''
    if mOperate["find_type"] == common.find_element_by_id or mOperate["find_type"] == common.find_element_by_xpath or mOperate["find_type"] == common.find_element_by_name or common.find_elements_by_class_name:
        elements_by(mOperate, cts).send_keys(mOperate["text"])
# 输入验证码，根据睡眠时间时间人工输入内容
def send_code():
    time.sleep(10)


