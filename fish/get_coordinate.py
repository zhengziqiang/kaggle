#coding=utf-8
import Image
import os
import numpy as np
from skimage import io
from PIL import Image, ImageStat 
root='/home/zzq/py-faster-rcnn/data/VOCdevkit2007/VOC2007/JPEGImages/'
dest='/home/zzq/dest/'
f=open('/home/zzq/output')
def write_mean(img_name,raw_name,cate,l):
	file=open('/home/zzq/kaggle/fish/dol_coor','a+')
	# str_=img_name+'\t'+cate+'\t'+('%n %n %n %n'%(l[0],l[1],l[2],l[3]))+'\n'
	str_=img_name+' '+cate+' '+str(l[0])+' '+str(l[1])+' '+str(l[2])+' '+str(l[3])+'\n'
	str_2=raw_name+' '+cate+' '+str(l[0])+' '+str(l[1])+' '+str(l[2])+' '+str(l[3])+'\n'
	file.write(str_)
	file.write(str_2)
lines=f.readlines()
for i in range(0,len(lines)):
	line=lines[i]
	line_=line.split()
	# print type(line_)
	# print line_
	img_name=line_[0]
	region=[]
	int_region=[]
	for j in range(2,6):
		region.append(float(line_[j]))
	img_path=root+img_name
	img=Image.open(img_path)
	# print region
	# img=io.imread(img_path)读取出来是一个numpy
	crop_img=img.crop(region)
	for zz in range(len(region)):
		int_region.append(int(region[zz]))
	rotate_img=crop_img.rotate(180)
	img.paste(rotate_img,int_region)
	raw_path_name=dest+'raw'+img_name
	raw_name='raw'+img_name
	img.save(raw_path_name)
	# star=ImageStat.Stat(crop_img)
	# l=[]
	# l=star.mean
	write_mean(img_name,raw_name,line_[1],int_region)


	# print img_name +'\t'+ line_[1]+ '\t'
	# print type(star.mean)
	# for k in range(len(star.mean)):
	# 	print l[k]


	# for  j in range(len(line_)):
	# 	print line_[j]
	
