from cv2 import cv2 as cv2 
import numpy as np
import copy
import math
img = cv2.imread('lena.bmp',0)
h1,w1 = img.shape
img = img.astype(np.float)

for i in range(1,h1-1,1):
    for j in range(1,w1-1,1):
        #print(i,j)
        if img[i][j]>=128:
            dummy=255  
        else:
            dummy=0
        error = img[i][j] - dummy
        #error = math.fabs(error)
        img[i][j] = dummy
        if (i<h1-1) and (j==0):
            img[i+1][j] = img[i+1][j] + error*5/13
            img[i][j+1] = img[i][j+1] + error*7/13 
            img[i+1][j+1] = img[i+1][j+1] + error*1/13
        elif (i<h1-1) and (j==w1-1):
            img[i+1][j] = img[i+1][j] + error*5/8
            img[i+1][j-1] = img[i+1][j-1] + error*3/8
        elif (i==h1-1) and (j<w1-1):
            img[i][j+1] = img[i][j+1] + error*7/7 
        elif (i<h1-1) and (j>0) and (j<w1-1):
            img[i+1][j] = img[i+1][j] + error*5/16
            img[i][j+1] = img[i][j+1] + error*7/16
            img[i+1][j+1] = img[i+1][j+1] + error*1/16
            img[i+1][j-1] = img[i+1][j-1] + error*3/16
        else:
            img[i][j]==img[i][j]
cv2.imwrite('ED_Floyd-steinberg.jpg', img*255)
cv2.imshow('ED',img)

cv2.waitKey(0)

    