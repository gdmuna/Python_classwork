import time  # 导入time模块
import random   # 导入random模块
from PIL import Image   # 导入PIL模块
# 定义计时器装饰器函数


def timer(func):    # 定义装饰器函数
    def wrap(*args, **kwargs):  # 定义包装函数
        begin_time = time.perf_counter()    # 记录函数开始时间
        result = func(*args, **kwargs)  # 执行函数
        end_time = time.perf_counter()  # 记录函数结束时间
        # 打印函数执行时间
        print(f'func:{func.__name__} took:{end_time - begin_time:.4f} sec')
        return result   # 返回函数执行结果
    return wrap  # 返回包装函数
# 定义文件信息分离函数


def split_info(file_info):  # 定义文件信息分离函数
    f_name, lab = file_info[0:-1].split(' ')    # 将文件名和标签分离
    return [f_name, lab]    # 返回文件名和标签
# 定义读取图像列表函数


@timer
def read_list(f_list):  # 定义读取图像列表函数
    for item in f_list:  # 遍历图像列表
        # 打开指定路径的图像
        img = Image.open(item[0])   # 打开图像


        # print(img.size)
# 主函数
if __name__ == "__main__":  # 判断是否为主函数
    # 打开指定文件，读取图像列表信息
    f = open("img_list")    # 打开文件
    info_list = f.readlines()   # 读取文件内容
    # 将图像列表信息分离成文件名和标签的列表
    file_list = list(map(split_info, info_list))    # 将文件信息分离
    # 随机打乱图像列表
    random.shuffle(file_list)   # 打乱图像列表
    # 计算训练集、验证集和测试集的偏移量
    r_train, r_val, r_test = 0.6, 0.2, 0.2  # 训练集、验证集和测试集的比例
    num = len(file_list)    # 图像列表的长度
    offset_val = int(num * r_train)  # 验证集的偏移量
    offset_test = offset_val + int(num * r_val)  # 测试集的偏移量
    # 根据偏移量将图像列表划分为训练集、验证集和测试集
    train_set = file_list[:offset_val]  # 训练集
    val_set = file_list[offset_val: offset_test]    # 验证集
    test_set = file_list[offset_test:]  # 测试集
    # 分别读取训练集、验证集和测试集中的所有图像
    read_list(train_set)    # 读取训练集
    read_list(val_set)  # 读取验证集
    read_list(val_set)  # 读取验证集
