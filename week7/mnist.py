#!usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cv2
import pickle
# 定义 mnist 类


class mnist(object):    # object是所有类的父类
    def __init__(self, filename):
        # 构造函数，打开图像数据文件，将数据读入到 img_list 中
        with open(filename, 'rb') as imgfile:   # 以二进制格式打开一个文件只用于读入，文件指针将会放在文件的开头。
            # 从文件中读取数据，并将数据转换为 Python 的数据结构
            self.img_list = pickle.load(imgfile)

    def __getitem__(self, idx):   # idx为指定的下标
        # 实现 __getitem__ 方法，用于获取指定下标的图像数据
        return self.img_list[idx]   # 返回指定下标的图像数据

    def __len__(self):  # self为类的实例
        # 实现 __len__ 方法，用于获取图像数据列表的长度
        return len(self.img_list)   # 返回图像数据列表的长度

 # 图像数据文件路径
filename = r'./imgdata/imgs.dat'    # r表示原生字符串
# 实例化 mnist 类
a = mnist(filename)  # a为类的实例
# 遍历图像数据列表，输出每个图像对应的标签，并将图像保存为 JPEG 格式
for i in range(a.__len__()):    # 遍历图像数据列表
    print(a.__getitem__(i)[1])  # 输出每个图像对应的标签
    cv2.imwrite('outimg/{}.jpg'.format(i),
                a.__getitem__(i)[0])  # 将图像保存为 JPEG 格式
