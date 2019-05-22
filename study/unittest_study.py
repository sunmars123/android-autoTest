#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/3 15:50 
# @Author : Zero 
# @Site :  
# @File : unittest_study.py 
# @Software: PyCharm
import unittest
from testDAL import HTMLTestRunner
class TestStringMethods(unittest.TestCase):
    # '''
    # 每个测试方法运行前运行，测试前的初始化工作。
    # '''
    # def setUp(self):
    #     print(0)
    # '''
    # 每个测试方法运行后运行，测试后的清理工作
    # '''
    # def tearDown(self):
    #     print(1)
    # '''
    # 所有测试方法运行前运行，整个测试过程只执行一次。必须用@classmethod修饰
    # '''
    # @classmethod
    # def setUpClass(cls):
    #     print("start")
    # '''
    # 所有测试方法运行后运行，整个测试过程只执行一次，单元测试后期清理。必须用@classmethod修饰
    # '''
    # @classmethod
    # def tearDownClass(cls):
    #     print("end")
    #
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print(22222)

    def test_run3(self):
        # self.assertEqual(1,1)
        self.assertTrue(1 == 1)
        # 测试用例

    def test_run1(self):
        # self.assertEqual(1,1)
        self.assertTrue(1 == 2)
        # 测试用例
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods("test_run1"))
    suite.addTest(TestStringMethods("test_run3"))
    runner = unittest.TextTestRunner()
    fp = open("res.html", "wb")
    r = HTMLTestRunner.HTMLTestRunner(stream=fp, title='all_tests', description='所有测试情况')
    r.run(suite)


