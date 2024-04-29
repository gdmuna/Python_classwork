import cv2  # 导入opencv库
import os   # 导入os库
import pickle   # 导入pickle库
 # 定义裁剪图像的函数
def cut_img(img_path):  
    # 读取指定路径的图像
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    # 将图像裁剪为256*256大小
    sub_img = cv2.resize(img,(256,256))
    return sub_img
 # 遍历指定路径下的所有文件
def walk_path(dir_path, img_list):
    for rootdir, dirs, f_names in os.walk(dir_path):
        for f_name in f_names:
            f_path = os.path.join(rootdir, f_name)
            sub_img = cut_img(f_path)
            img_list.append([sub_img, rootdir]) 
    return
if __name__ == "__main__":
    img_dir = './imgs'
    img_list = []
     # 遍历图像文件夹，并裁剪图像，将裁剪后的图像和目录信息存储在列表中
    walk_path(img_dir, img_list)
     # 将列表写入磁盘文件
    f = open('save_img', 'wb')
    pickle.dump(img_list, f)
    f.close()