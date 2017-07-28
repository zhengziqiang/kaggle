#coding=utf-8
import Image
import os
import numpy as np
from skimage import io
from PIL import Image, ImageStat 
root='/home/zzq/py-faster-rcnn/data/VOCdevkit2007/VOC2007/JPEGImages/'
f=open('/home/zzq/kaggle/fish/fish_coorderation')
def write_coor(img_name,line,l,mid_h,mid_w):
	l_new=[]
	
