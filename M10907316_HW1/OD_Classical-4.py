from cv2 import cv2 as cv2
import numpy as np


img = cv2.imread('lena.jpg',0)
h1,w1 = img.shape


imgnews=np.empty((512,512))
DA=np.array([[0.567 ,0.635, 0.608, 0.514, 0.424, 0.365, 0.392, 0.486],
    [0.847, 0.878, 0.910, 0.698, 0.153, 0.122, 0.090, 0.302],
    [0.820, 0.969, 0.941, 0.667, 0.180, 0.031, 0.059, 0.333],
    [0.725, 0.788, 0.757, 0.545, 0.275, 0.212, 0.243, 0.455],
    [0.424, 0.365, 0.392, 0.486, 0.567, 0.635, 0.608, 0.514],
    [0.153, 0.122, 0.090, 0.302, 0.847, 0.878, 0.910, 0.698],
    [0.180, 0.031, 0.059, 0.333, 0.820, 0.969, 0.941, 0.667],
    [0.275, 0.212, 0.243, 0.455, 0.725, 0.788, 0.757, 0.545]])
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
cv2.imwrite('OD_Classical-4.jpg', imgnews)
cv2.imshow('Classical-4',imgnews)
cv2.waitKey(0)