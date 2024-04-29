# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 23:13
# @Author  : play4fun
# @File    : OpenCV图像坐标系_test.py
# @Software: PyCharm
"""
OpenCV图像坐标系_test.py:
"""
import cv2
import os
import pickle
# 定义裁剪图像的函数


def cut_img(img_path):
    # 读取指定路径的图像
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    print('img.shape:', img.shape)  # (512, 512, 3)
    # 将图像裁剪为256*256大小
    sub_img = cv2.resize(img, (256, 256))   # cv2.resize()函数实现图像的缩放
    return sub_img
 # 遍历指定路径下的所有文件和子目录，并将裁剪后的图像和对应的目录信息存储在列表中


def walk_path(path, f_list):
    # 获取指定路径下的所有文件和子目录
    dir_items = os.listdir(path)    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    for d_item in dir_items:    # 遍历当前目录下的所有文件和子目录
        d_path = os.path.join(path, d_item)   # 获取文件或子目录的绝对路径
        # 如果是文件，则将其裁剪后的图像和对应的目录信息存储在列表中
        if os.path.isfile(d_path):  # os.path.isfile() 方法用于判断对象是否为一个文件。
            sub_img = cut_img(d_path)   # 调用cut_img函数裁剪图像
            lab = os.path.split(path)[-1]       # 获取文件所在的目录名
            f_list.append([sub_img, lab])   # 将裁剪后的图像和对应的目录信息存储在一个二维列表中
        # 如果是子目录，则递归调用遍历函数，继续遍历子目录
        if os.path.isdir(d_path):   # os.path.isdir() 方法用于判断对象是否为一个目录。
            walk_path(d_path, f_list)   # 递归地遍历子目录下的文件


if __name__ == "__main__":
    # 指定要遍历的根目录
    rootdir = './imgs'
    file_list = []
    # 遍历目录并裁剪图像，将裁剪后的图像和目录信息存储在列表中
    walk_path(rootdir, file_list)   # 递归遍历指定目录下的所有文件和子目录
    # 将列表写入磁盘文件
    f = open("cutted_imgs", "wb")   # 以二进制写模式打开文件
    pickle.dump(file_list, f)   # 将列表写入磁盘文件
    f.close()
    img_list = []   # 定义一个列表，用于存储从磁盘文件中读取的列表信息
    # 从磁盘文件中读取列表信息
    f = open("cutted_imgs", "rb")   # 以二进制读模式打开文件
    img_list = pickle.load(f)   # 从磁盘文件中读取列表信息
    # 显示裁剪后的所有图像
    for idx, sub_img in enumerate(img_list):    # 遍历列表中的每个元素
        cv2.imshow('src', sub_img[0])   # 显示图像
        cv2.waitKey(0)  # 等待按键按下
