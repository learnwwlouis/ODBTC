# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:45:47 2022

@author: a23a23atw
"""

import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

rawData = open( "lena.RAW" ,'rb').read() 
im = Image.frombytes("L", (512,512), rawData) 
ori=np.array(im)
img=np.array(im)
rows,cols=img.shape
plt.figure("original")
plt.imshow(img,cmap='gray')
print(img)
#--------------------------------------------------------------------
size=8

D=[[0.513,0.272,0.724,0.483,0.543,0.302,0.694,0.453],
   [0.151,0.755,0.091,0.966,0.181,0.758,0.121,0.936],
   [0.634,0.392,0.574,0.332,0.664,0.423,0.604,0.362],
   [0.060,0.875,0.211,0.815,0.030,0.906,0.241,0.845],
   [0.543,0.302,0.694,0.453,0.513,0.272,0.724,0.483],
   [0.181,0.758,0.121,0.936,0.151,0.755,0.091,0.966],
   [0.664,0.423,0.604,0.362,0.634,0.392,0.574,0.332],
   [0.030,0.906,0.241,0.845,0.060,0.875,0.211,0.815]
]
D=np.array(D)
AV=[]
a=[]
b=[]
d=512//size
nextimg=np.zeros((512,512),dtype=np.int)
rows,cols=img.shape
for i in range(d):
    for j in range(d):
        SUM=0
        MAX=0
        MIN=257
        for ii in range(size):
            for jj in range(size):
                SUM+=img[i*size+ii,j*size+jj] 
                if(MAX<img[i*size+ii,j*size+jj]):
                    MAX=img[i*size+ii,j*size+jj]
                if(MIN>img[i*size+ii,j*size+jj]):
                    MIN=img[i*size+ii,j*size+jj]
        AV.append(SUM//(size*size))
        a.append(MIN)
        b.append(MAX)
n=0
for i in range(d):
    for j in range(d):
        bb=b[n]
        aa=a[n]
        for ii in range(size):
            for jj in range(size):
                target=img[i*size+ii,j*size+jj]
                DD=((bb-aa)*(D[ii,jj]-D.min())/(D.max()-D.min()))
                if(target>=DD+aa):
                    img[i*size+ii,j*size+jj]=bb
                else:
                    img[i*size+ii,j*size+jj]=aa
        n+=1

plt.figure("test")
plt.imshow(img,cmap='gray')
print(img)

        

