#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/13 14:18 
# @Author : Zero 
# @Site :  
# @File : OperateFile.py 
# @Software: PyCharm
import os
class OperateFile:
    def __init__(self, file, method="w+"):
        self.file = file
        self.method = method
        self.fileHandle = None
    '''
    写入文件
    '''
    def write_txt(self, line):
        if OperateFile(self.file).check_file() is False:
            self.mkdir_file()
        self.fileHandle = open(self.file, self.method)
        self.fileHandle.write(line + "\n")
        self.fileHandle.close()
    '''
    单行读取文件
    '''
    def read_txt_row(self):
        resutl = ""
        if OperateFile(self.file).check_file():
            self.fileHandle = open(self.file, self.method)
            resutl = self.fileHandle.readline()
            self.fileHandle.close()
        return resutl
    '''
    多行读取
    '''
    def read_txt_rows(self):
        if OperateFile(self.file).check_file():
            self.fileHandle = open(self.file, self.method)
            file_list = self.fileHandle.readlines()
            for i in file_list:
                print(i.strip("\n"))
            self.fileHandle.close()
    '''
    检查文件
    '''
    def check_file(self):
        if not os.path.isfile(self.file):
            # print('文件不存在' + self.file)
            # sys.exit()
            return False
        else:
            return True
        # print("文件存在！")
    '''
    创建文件
    '''
    def mkdir_file(self, method="w+"):
        if not os.path.isfile(self.file):
            f = open(self.file, method)
            f.close()
            print("创建文件成功")
        else:
            print("文件已经存在")
    def remove_file(self):
        if os.path.isfile(self.file):
            os.remove(self.file)
            print("删除文件成功")
        else:
            print("文件不存在")