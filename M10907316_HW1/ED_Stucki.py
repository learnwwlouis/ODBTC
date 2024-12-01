from cv2 import cv2 as cv2 
import numpy as np
import copy
import math
img = cv2.imread('lena.bmp',0)
h1,w1 = img.shape
img = img.astype(np.float)

kernel = np.array([[0,0,0,8,4],
                [2,4,8,4,2],
                [1,2,4,2,1]])

for i in range(0,h1-1,1):
    for j in range(0,w1-1,1):
        #print(i,j)
        if img[i][j]>=128:
            dummy=255  
        else:
            dummy=0
        error = img[i][j] - dummy
        #error = math.fabs(error)
        img[i][j] = dummy
        kernel_sum = 0
        for x in range(0,kernel.shape[0]):
            for y in range(0,kernel.shape[1]):
                if (i+x>=0) and (j+y>=2) and (i+x<h1) and (j+y<w1):
                    kernel_sum+=kernel[x][y]
                    
        for x in range(0,kernel.shape[0]):
            for y in range(0,kernel.shape[1]):
                if (i+x>=0) and (j+y>=2) and (i+x<h1) and (j+y<w1):
                    img[i+x][j+y-2] = img[i+x][j+y-2] + (error*kernel[x][y]/kernel_sum)
                    
cv2.imwrite('ED_Stucki.jpg', img)
cv2.imshow('ED',img)
cv2.waitKey(0)