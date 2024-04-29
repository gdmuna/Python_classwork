import cv2  # 导入OpenCV库
import os   # 导入os库
import pickle   # 导入pickle库
# 定义一个裁剪图像的函数


def cut_img(img_path):
    # 读取指定路径的图像
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    # 将图像裁剪为256*256大小
    sub_img = cv2.resize(img, (256, 256))
    return sub_img  # 返回裁剪后的图像
 # 遍历指定路径下的所有文件


def walk_path(path, f_list, cur_dir=''):
    for rootdir, dirs, f_names in os.walk(path):
        for f_name in f_names:      # 遍历当前目录下的所有文件
            path = os.path.join(rootdir, f_name)  # 获取文件的绝对路径
            sub_img = cut_img(path)     # 调用cut_img函数裁剪图像
            f_list.append([sub_img, cur_dir])    # 将裁剪后的图像和对应的目录信息存储在一个二维列表中
        for dir in dirs:    # 遍历当前目录下的所有子目录
            sub_dir = os.path.join(path, dir)    # 获取子目录的绝对路径
            # 递归地遍历子目录下的文件
            walk_path(sub_dir, f_list, cur_dir=dirs)


if __name__ == '__main__':
    # 指定待处理图像所在目录的路径
    rootdir = './imgs'
    file_list = []
    # 遍历目录下的所有文件，并将裁剪后的图像和对应的目录信息存储在一个二维列表中
    walk_path(rootdir, file_list)
    # 将裁剪后的图像列表写入到一个磁盘文件中
    f = open("cutted_imgs", "wb")
    pickle.dump(file_list, f)
    f.close()
    img_list = []
    # 从磁盘文件中读取裁剪后的图像列表
    f = open("cutted_imgs", "rb")
    img_list = pickle.load(f)
 #     for idx,sub_img in enumerate(img_list):
#         cv2.imshow('src',sub_img[0])
#         cv2.waitKey(0)
