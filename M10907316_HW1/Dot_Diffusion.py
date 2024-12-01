from cv2 import cv2 as cv2 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import math
img = cv2.imread('lena.jpg',0)
height, width = img.shape[:2]
threshold = 128
imgnew = np.empty((height,width))
pattern = np.array([[42,47,46,45,16,13,11,2],
	[61,57,53,8,27,22,9,50],
	[63,58,0,15,26,31,40,30],
	[10,4,17,21,3,44,18,6],
	[14,24,25,7,5,48,52,39],
	[20,28,23,32,38,51,54,60],
	[19,33,36,37,49,43,56,55],
	[12,62,29,35,1,59,41,34]])
patMaps = np.zeros((height,width))
pheight, pwidth = pattern.shape[:2]
totheight = int(height / pheight)
totwidth = int(width / pwidth)
patProc = np.empty((pheight*pwidth,2))
for m in range(0,pheight):
	for n in range(0,pwidth):
		patProc[pattern[m][n]][0] = m
	
		patProc[pattern[m][n]][1] = n
img = img.astype(float)
pattern = pattern.astype(float)
weight = np.array([[0.271630,1,0.271630],
	                [1,0,1],
	                [0.271630,1,0.271630]])
dumArray = np.copy(img)
for i in range(0,height,pheight):
	for j in range(0,width,pwidth):
		#print(i,j)
		index = 0
		while index != (pheight * pwidth):
			ni = int(i + patProc[index][0])
			nj = int(j + patProc[index][1])
			
			if dumArray[ni][nj] > threshold:
				dummy = 255
			else:
				dummy = 0
			error = dumArray[ni][nj] - dummy
			img[ni][nj] = dummy
			patMaps[ni][nj] = 1
			
			fm = 0
			for m in range(-1,2):
				for n in range(-1,2):
					if (ni+m >= 0) and (ni+m < height) and (nj+n >= 0) and (nj+n < width):
						if patMaps[ni+m][nj+n] == 0:
							fm = fm + weight[m+1][n+1]

			for m in range(-1,2):
				for n in range(-1,2):
					if (ni+m >= 0) and (ni+m < height) and (nj+n >= 0) and (nj+n < width):
						if patMaps[ni+m][nj+n] == 0:
							dumArray[ni+m][nj+n] = dumArray[ni+m][nj+n] + (error * weight[m+1][n+1] / fm)

			index = index + 1
cv2.imwrite('Dot_Diffusion.jpg',img)
cv2.imshow("DD",img)
cv2.waitKey(0)
cv2.destroyAllWindows()