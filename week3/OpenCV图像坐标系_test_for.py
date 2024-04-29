# Python代码，需要在Python环境下运行
# 修改图像程序，使其可以搜索指定目录下所有照片，并裁剪每张图片为统一的256*256，把所有裁剪后的图片放入存储在一个磁盘文件中。
"""
OpenCV图像坐标系_test.py:
"""
# 导入必要的库文件
from fileinput import filename
import cv2
import os
import pickle
print(1, '-'*50)
print(__name__)
# 定义一个裁剪图像的函数


def cut_img(img_path):
    # 读取指定路径的图像
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    print('img.shape:', img.shape)
    # 设置新图像的大小为256*256，并保持图像长宽比不变
    sub_img = cv2.resize(img, (256, 256))
    # 返回裁剪后的图像
    return sub_img


 # 如果当前文件被执行，则执行以下代码
if __name__ == "__main__":
    # 设置图片所在目录的路径
    rootdir = './imgs'
    # 获取目录中的所有文件名
    list = os.listdir(rootdir)
    img_list = []
    # 遍历目录下的所有文件，对每个文件进行裁剪
    for idx, filename in enumerate(list):
        # 拼接文件的完整路径
        path = os.path.join(rootdir, filename)
        # 裁剪指定路径的图像
        sub_img = cut_img(path)
        # 将裁剪后的图像放入一个列表中
        img_list.append(sub_img)
     # 将裁剪后的图像列表写入到一个磁盘文件中
    f = open("cutted_imgs", "wb")
    pickle.dump(img_list, f)
    # 从磁盘文件中读取裁剪后的图像列表
    f = open("cutted_imgs", "rb")
    img_list = pickle.load(f)
    # 遍历裁剪后的图像列表，并在窗口中显示每个图像
    for idx, sub_img in enumerate(img_list):
        # 在窗口中显示指定的图像
        cv2.imshow('src', sub_img)
        # 等待按下任意按键
        cv2.waitKey(0)
