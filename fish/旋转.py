#coding=utf-8
import Image  
import glob, os
def albimage():  
    for files in glob.glob('/home/zzq/kaggle/picture/*.JPG'):  
        filepath,filename = os.path.split(files)  
        filterame,exts = os.path.splitext(filename)  
        #输出路径  
        opfile = r'/home/zzq/kaggle/picture_all/'  
        #判断opfile是否存在，不存在则创建  
        if (os.path.isdir(opfile)==False):
            print 'not exist'  
            os.mkdir(opfile)  
        im = Image.open(files)  
        #w,h = im.size  
        #im_ss = im.resize((960,1280))  
        #im_ss = im.convert('P')
        #items=[45,90,135,180,225,270,315]
        #for item in range(46):
            #im_ss=im.rotate(item)
        #str_item=str(item)
        #im_ss = im.resize((int(w*0.12), int(h*0.12)))  
        #im_ss=im.rotate(90)
        im.save(opfile+filterame+'.jpg')  
        #im_ss=im.rotate
if __name__=='__main__':
    albimage()