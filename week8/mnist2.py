#!usr/bin/env python
# -*- coding: utf-8 -*-
import os   #导入模块
import cv2  #导入模块
import pickle #导入模块
class mnist:#创建父类
    def __init__(self, filename):#构造方法
        with open(filename, 'rb') as imgfile:   #打开文件   #以二进制格式打开一个文件只用于读入，文件指针将会放在文件的开头。
            self.img_list = pickle.load(imgfile)    #读取文件   #从文件中读取数据，并将数据转换为 Python 的数据结构
    def __getitem__(self, idx):    # idx为指定的下标   #实现 __getitem__ 方法，用于获取指定下标的图像数据  
        return self.img_list[idx]   #返回图像数据   #实现 __getitem__ 方法，用于获取指定下标的图像数据
    def __len__(self): # self为类的实例   #实现 __len__ 方法，用于获取图像数据列表的长度
        return len(self.img_list)   #返回图像数据列表的长度   #实现 __len__ 方法，用于获取图像数据列表的长度
class reszie_mnist(mnist):  #创建子类
    def __init__(self, filename, size): 
        # 继承父类并添加新属性
        self.size = size    #新属性  #构造函数，打开图像数据文件，将数据读入到 img_list 中
        mnist.__init__(self, filename)  #继承父类
    def __resize__(self, idx):
        # 实现 __resize__ 方法，用于修改指定下标的图像大小
        self.img_list[idx][0] = cv2.resize(self.img_list[idx][0],self.size) #修改指定下标的图像大小 
    def __getitem__(self, idx): # idx为指定的下标
        # 在调用父类 __getitem__ 方法前，先调用 __resize__ 方法将图像大小进行修改
        self.__resize__(idx)    #调用 __resize__ 方法将图像大小进行修改
        return self.img_list[idx]   #返回图像数据   #实现 __getitem__ 方法，用于获取指定下标的图像数据
 # 图像数据文件路径
filename = 'imgs.dat'   #图像数据文件路径
# 实例化 reszie_mnist 子类
a = reszie_mnist(filename, size=[64, 64])   #实例化 reszie_mnist 子类
# 遍历图像数据列表，输出每个图像对应的标签，并将修改后的图像保存为 JPEG 格式
for i in range(a.__len__()):    #遍历图像数据列表   
    # 获取图像及其对应的标签
    img, lab = a.__getitem__(i) #获取图像及其对应的标签
    # 输出图像对应的标签
    print(lab)  #输出图像对应的标签
    # 将图像保存为 JPEG 格式
    cv2.imwrite('outimg/{}.jpg'.format(i),img)  #将图像保存为 JPEG 格式