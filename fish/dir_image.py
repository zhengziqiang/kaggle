#coding=utf-8
from skimage import data_dir,io,transform,color
import numpy as np
import Image
import cv2
def convert_gray(f):
     rgb=io.imread(f)    #依次读取rgb图片
     im2=rgb.getRotationMatrix2D(center,45,0.75)  #将rgb图片转换成灰度图
     #dst=transform.resize(gray,(256,256))  #将灰度图片大小转换为256*256
     return im2
    
str="/home/zzq/kaggle/LAG/"+'/*.jpg'
coll = io.ImageCollection(str,load_func=convert_gray)
for i in range(len(coll)):
    io.imsave('/home/zzq/kaggle/lag_45/'+np.str(i)+'.jpg',coll[i])  #循环保存图片