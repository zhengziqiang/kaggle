#coding=utf-8
import Image  
import glob, os  

def raw_image(img_nmae):  
    img_all_path_name='/home/zzq/kaggle/py_dataaug/' + img_nmae +'/*.jpg'
    #print img_all_path_name
    for files in glob.glob(img_all_path_name):  
        filepath,filename = os.path.split(files)  
        filterame,exts = os.path.splitext(filename)  
        #输出路径  
        #opfile = r'/home/zzq/kaggle/py_dataaug/ALB_all/' 

        opfile= '/home/zzq/kaggle/py_dataaug/' + img_nmae +'_all/'
        #判断opfile是否存在，不存在则创建  
        if (os.path.isdir(opfile)==False):
            print 'not exist'  
            os.mkdir(opfile)  
        im = Image.open(files)  
        #w,h = im.size  
        #im_ss = im.resize((400,400))  
        #im_ss = im.convert('P')
        items=[45,90,135,180,225,270,315,360]
        for item in items:
            im_ss=im.rotate(item)
            str_item=str(item)
            #im_ss = im.resize((int(w*0.12), int(h*0.12)))  
            im_ss.save(opfile+filterame+str_item+'.jpg') 

if __name__ == '__main__':
    raw_image('ALB')
    # img_name_lists=['BET','DOL','LAG','NoF','OTHER','SHARK','YFT']
    # for img_name in img_name_lists:
    #     raw_image(img_name)
