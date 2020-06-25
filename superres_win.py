import tensorflow as tf
from model.rtsr import rtsr
import d3dshot
import numpy as np
import cv2
import time
from PIL import Image

tf.keras.backend.set_floatx('float16')

myrtsr=rtsr(scale=4, num_res_blocks=4,lastlayerdivide=2)
myrtsr.load_weights('weights/myedsr-lastdiv2_4block-x4_weights.h5')
inp=myrtsr.input
out=tf.keras.backend.clip(myrtsr.output, 0, 255)
myclippededsr=tf.keras.models.Model(inputs=inp, outputs=out)


pixels=[2,2]
shiftzero=[0,0]
windowsize=[0,0]
FPS=10.0
enhance=False
dimensions=(60,60,60+640,60+480)
d = d3dshot.create(capture_output="numpy")

while True:
    starttime=time.time()
    screen=d.screenshot(region=(dimensions[0]//8*8+shiftzero[0],dimensions[1]//8*8+shiftzero[1],dimensions[2]//8*8+shiftzero[0]+windowsize[0],dimensions[3]//8*8+shiftzero[1]+windowsize[1]))
    imageinit=screen[:,:,:3][:,:,::-1]
    img2 = np.array(Image.fromarray(imageinit).resize((imageinit.shape[1]//pixels[1],imageinit.shape[0]//pixels[0])))
    if enhance==False:
        img3=np.array(Image.fromarray(imageinit).resize((imageinit.shape[1]*4//pixels[1],imageinit.shape[0]*4//pixels[0]),Image.NEAREST))
    if enhance==True:
        img3=myclippededsr.predict(np.expand_dims(img2, 0))[0]
    img5=img3.astype(np.uint8)
    cv2.putText(img5,'FPS {:.2f} SR {}'.format(FPS, enhance),(30,30),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,255),thickness=1)
    cv2.imshow('RTSR', img5)
    k = cv2.waitKey(1) 
    if k == ord('0'):
        enhance=1-enhance
    if k == ord('1'):
        pixels[1]=1
        pixels[0]=1
    if k == ord('2'):
        pixels[1]=2
        pixels[0]=2
    if k == ord('w'):
        shiftzero[1]=shiftzero[1]+1
    if k == ord('s'):
        shiftzero[1]=shiftzero[1]-1
    if k == ord('a'):
        shiftzero[0]=shiftzero[0]+1
    if k == ord('d'):
        shiftzero[0]=shiftzero[0]-1
    if k == ord('k'):
        windowsize[1]=windowsize[1]+8
    if k == ord('i'):
        windowsize[1]=windowsize[1]-8
    if k == ord('j'):
        windowsize[0]=windowsize[0]+8
    if k == ord('l'):
        windowsize[0]=windowsize[0]-8
    if k == ord('q'):
        cv2.destroyAllWindows()
        break
    FPS=1/(time.time()-starttime)
