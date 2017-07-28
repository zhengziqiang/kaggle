import numpy
from PIL import Image
from pylab import *
from skimage import io,data
im=array(Image.open('/home/zzq/6.jpg'))
im_c=im[:,:,0]
im_r=np.zeros((64,64))
im_r=im_c
out=file('/home/zzq/2/1.txt','w')
for i in range(64):
	for j in range(64):
		out.write(str(im_r[i][j])+' ')
	out.write('\n')
out.close()
print type(im_r)
print im_r.shape
for i in range(64):
    for j in range(64):
        print im_r[i][j]
        if im_r[i][j] > 200:
            # im_r[i][j]=np.random.uniform(64,78)
            im_r[i][j]-=180
            im_r[i][j]*=1.984
            continue
        else:
            if im_r[i][j] > 150:
                # im_r[i][j]=np.random.uniform(30,50)
                im_r[i][j]-=150
                im_r[i][j]*=0.7
                continue
            else:
                if im_r[i][j] > 80:
                    # im_r[i][j]=np.random.uniform(20,30)
                    im_r[i][j]-=80.0
                    im_r[i][j]*=0.7
                    continue
                else:
                    if im_r[i][j] >40:
                        im_r[i][j]-=40.0
                        im_r[i][j]*=0.3
                    else:
                        im_r[i][j]*0.18
                    # im_r[i][j]=np.random.uniform(0,20)



zzq=im_r
new_im=Image.fromarray(zzq).convert('L')
new_im.save('/home/zzq/dest/1.jpg')