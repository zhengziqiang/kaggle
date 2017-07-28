#coding=utf-8

from PIL import Image
import glob,os
from skimage import io,data
from pylab import *
for files in glob.glob('/home/zzq/kaggle/green/test.jpg'):  
	filepath,filename = os.path.split(files)  
	filterame,exts = os.path.splitext(filename)  
	#输出路径  
	opfile = r'/home/zzq/kaggle/normal/'  
	#判断opfile是否存在，不存在则创建  
	if (os.path.isdir(opfile)==False):
		print 'not exist'  
		os.mkdir(opfile)
	im=array(Image.open(files))
	g=im[:,:,1]
	# for i in g:
	# 	if ((i>30).any()):
	# 		i-=30
	# 	else:
	# 		i=1
	#print g.shape()
	a=256
	for row in g:
		for i in row:
			if (a>i):
				a=i
			else:
				pass
	g-=a
	im[:,:,1]=g
	#im2=imshow(im)
	new_im = Image.fromarray(im)
	new_im.save(opfile+filename+'.jpg')
