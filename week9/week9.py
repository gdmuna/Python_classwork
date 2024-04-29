import cv2  # 导入 cv2 模块
path = r'./save_4_5.txt'  # 保存图像路径和标签的文件


class training():   # 定义 training 类
    def __init__(self, path):    # 构造函数
        with open(path, 'r') as f:  # 打开保存图片路径和标签的文件
            self.data = f.readlines()  # 将读取到的数据保存在data中
        f.close()   # 关闭文件
        self.datas = []   # 保存图像路径和标签的列表
        for i in range(len(self.data)):  # 遍历data中的数据
            photo_path, photo_label = self.data[i].split(
                ':')  # 将路径和标签分割，这里用冒号进行分割
            self.datas.append([photo_path, photo_label[0]]
                              )  # 保存路径和标签的列表添加到datas列表中

    def __getitem__(self, index):  # 获取指定下标的图片和标签
        path, label = self.data[index].split(':')  # 使用冒号分割，将路径和标签分开
        return path, label.rstrip()  # 返回路径和标签，同时去掉标签的换行符

    def __len__(self):  # 获取数据集中的样本数
        return len(self.data)   # 返回数据集中的样本数


class trainings(training):  # 定义 trainings 类，继承 training 类
    def __resize__(self, img):
        # 图像缩放
        img = cv2.resize(img, (90, 128))    # 将图像缩放为90*128大小
        return img  # 返回缩放后的图像

    def __getitem__(self, index):    # 获取指定下标的图像和标签
        try:
            # 获取指定下标的图像和标签
            image_path, label = self.datas[index]
            # 读取图像
            image = cv2.imread(image_path)
            # 调用 __resize__ 方法缩放图像
            image = self.__resize__(image)
            return image, label
        except:
            # 如果出现错误，什么也不做，继续下一次迭代
            pass

 # 实例化 trainings 类
train = trainings(path)
# 输出第 30 张图像及其对应的标签
print(train[30])
