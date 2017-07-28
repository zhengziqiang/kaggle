#coding=utf-8
import Image
import os

#裁剪图片实例
# f=open('demo')
# print f.read()
# print type(f)
# n=f.read()
# print n
# img=Image.open('000456.jpg')
# region=(80.1743,46.1868,422.162,298.323)
# region2=(137.606
# ,120.404
# ,169.998
# ,158.271)
# crop_img=img.crop(region2)
# crop_img.save('crop.jpg')

# f=open('demo','a')
# n=[1,2,3,4]
# for i in n:
# 	f.write(str(i)+'\t')
# f.write('\n')
# f.close()

#从文件中读取位置信息
# i=1
# f=open('demo')
# while 1:
# 	line=f.readline()
# 	if not line:
# 		break
# 	# print type(line) str
# 	# line.strip('\t')
# 	line.split()
# 	print type(line)
# 	print line
# 	# l=int(line)
# # 	# print l



# img=Image.open('/home/zzq/py-faster-rcnn/data/demo/image_00003.jpg')
# newimg=img.resize(900,900)
# newimg.save('newimg.jpg')



# def ResizeImage(filein, fileout, width, height, type):
#     img = Image.open(filein)
#     out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
#     out.save(fileout, type)

# filein = r'/home/zzq/py-faster-rcnn/data/demo/image_00003.jpg'
# fileout = r'/home/zzq/test.jpg'
# width = 60
# height = 85
# type = 'jpeg'
# ResizeImage(filein, fileout, width, height, type)


img=Image.open('/home/zzq/py-faster-rcnn/data/demo/image_00003.jpg')
print img.size
region=[300,75,900,675]
crop_img=img.crop(region)
crop_img.show()