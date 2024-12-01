from cv2 import cv2 as cv2 
import numpy as np


img = cv2.imread('lena.jpg',0)
h1,w1 = img.shape


imgnews=np.empty((512,512))
DA=np.array([[0.513, 0.272, 0.724, 0.483, 0.543, 0.302, 0.694, 0.453],
    [0.151, 0.755, 0.091, 0.966, 0.181, 0.758, 0.121, 0.936],
    [0.634, 0.392, 0.574, 0.332, 0.664, 0.423, 0.604, 0.362],
    [0.060, 0.875, 0.211, 0.815, 0.030, 0.906, 0.241, 0.845],
    [0.543, 0.302, 0.694, 0.453, 0.513, 0.272, 0.724, 0.483],
    [0.181, 0.758, 0.121, 0.936, 0.151, 0.755, 0.091, 0.966],
    [0.664, 0.423, 0.604, 0.362, 0.634, 0.392, 0.574, 0.332],
    [0.030, 0.906, 0.241, 0.845, 0.060, 0.875, 0.211, 0.815]])
h2,w2 = DA.shape
DA=DA*255
img = img.astype(np.float)
for i in range(0,h1):
    for j in range(0,w1):
        a = i % 8
        b = j % 8
        if img[i][j]>DA[a][b]:
            imgnews[i][j]=255
        else:
            imgnews[i][j]=0 
cv2.imwrite('OD_Bayer-5.jpg', imgnews)
cv2.imshow('Bayer-5',imgnews)
cv2.waitKey(0)