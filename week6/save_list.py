# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 23:13
# @Author  : play4fun
# @File    : OpenCV图像坐标系_test.py
# @Software: PyCharm
"""
OpenCV图像坐标系_test.py: 本脚本用于生成图像列表
"""
import cv2  # 导入OpenCV库
import os   # 导入os库
import pickle   # 导入pickle库
import numpy as np  # 导入numpy库
# 遍历指定路径下所有文件，获取文件路径及标签，并返回列表


def walk_path(path):    # path为指定的路径
    f_list = []    # 定义列表，用于存储图像路径及标签
    # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
    for rootdir, dirs, f_names in os.walk(path):
        for f_name in f_names:  # 遍历当前目录下的所有文件
            img_path = os.path.join(rootdir, f_name)    # 获取文件的绝对路径
            lab = os.path.split(rootdir)[-1]        # 获取文件所在的目录名
            f_list.append([img_path, lab])   # 将文件路径和标签存入列表
    return f_list   # 返回图像路径及标签列表


if __name__ == "__main__":
    # 指定图像路径
    rootdir = 'week6\\imgs'  # 指定图像路径
    file_list = []
    # 遍历图像路径下所有图像文件，获取图像路径及标签，并存入列表
    file_list = walk_path(rootdir)  # 调用walk_path函数遍历图像路径下所有图像文件
    # 将图像列表写入文件中
    f = open("img_list", 'w')    # 打开文件
    for file_info in file_list:  # 遍历图像列表
        f.write(f'{file_info[0]} {file_info[1]}\n')  # 将图像路径和标签写入文件中
    f.close()   # 关闭文件
