# -*- coding: utf-8 -*-
import cv2
# 读取图片butterfly.jpg，IMREAD_UNCHANGED意味着原尺寸读入图像
img = cv2.imread('./data/butterfly.jpg', cv2.IMREAD_UNCHANGED)  # 读取图片  
# 打印图片形状
print('img.shape:', img.shape)
# 读取图片opencv_logo.png，IMREAD_UNCHANGED意味着原尺寸读入图像
logo = cv2.imread('./data/opencv_logo.png', cv2.IMREAD_UNCHANGED)
# 处理logo尺寸，将logo大小调整为20×20像素
logo = cv2.resize(logo, (20, 20))
# 打印logo形状
print('logo.shape:', logo.shape)
# 读取图片butterfly.jpg，IMREAD_UNCHANGED意味着原尺寸读入图像
butterfly = cv2.imread('./data/butterfly.jpg', cv2.IMREAD_UNCHANGED)
# 处理butterfly尺寸，将butterfly大小调整为20×20像素
butterfly = cv2.resize(butterfly, (20, 20))
# 打印butterfly形状
print('butterfly.shape:', butterfly.shape)
# 在窗口中显示src图像，并将窗口移到窗口左上角
cv2.imshow('src', img)
cv2.moveWindow('src', 0, 0)
# 读取像素点(y, x)的BGR值
y = 100
x = 50
(b, g, r) = img[y, x]
# 打印BGR值到屏幕中
print('bgr:', b, g, r)
# 图像修改
# img[y:y+h,x:w]
# Y是行坐标，X是列坐标。对于Python数组和OpenCV数组，行是第一维，列是第二维
# 将logo复制到img的指定区域上，logo需要切掉第三维（alpha）
img[100:100 + logo.shape[0], 300:300 +
    logo.shape[1]] = logo[:, :, 0:3]  # 两张图片的shape不一样
# 将butterfly复制到img的指定区域上，butterfly需要切掉第三维（alpha）
img[300:300 + logo.shape[1], 100:100 + logo.shape[0]] = butterfly[:, :, 0:3]
# 在img上添加文本
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text='col=width=X0,row=height-Y0', org=(0, 0), fontFace=font, fontScale=0.5,   
            color=(0, 255, 0), thickness=2, bottomLeftOrigin=False)  # 文本内容、位置、字体、大小、颜色以及字体粗细
cv2.putText(img, text='col=width=X10,row=height-Y30', org=(10, 30), 
            fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)   
cv2.putText(img, text='col=width=X100,row=height-Y300', org=(100, 300),
            fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)   
cv2.putText(img, text='col=width-X300,row=height-Y100', org=(300, 100),
            fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)   
# 在窗口中显示修改后的img，并将窗口移到（x=img.shape[0], y=0）处
cv2.imshow('img+logo', img)
# 保存修改后的图像
cv2.imwrite('img_logo.jpg', img)
cv2.moveWindow('img+logo', x=img.shape[0], y=0)
cv2.waitKey(0)
