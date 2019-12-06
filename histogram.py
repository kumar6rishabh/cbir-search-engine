import cv2
import numpy as np
import collections
import matplotlib.pyplot as plt
import os
import csv

t = []
fir = []
sec = []
os.chdir('./new_dataset')
x = os.listdir()
ellipMask = np.zeros((700 , 700) , dtype = "uint8")
new_ellipMask = np.resize(ellipMask , (700 , 700 , 3))
test = cv2.ellipse(new_ellipMask , (350 , 350) , (200 , 150) , 0 , 0 , 360 , 255 , -1)
for i in range(700):
    for j in range(700):
        if(test[i][j][0] != 0):
            test[i][j][0] = 255
            test[i][j][1] = 255
            test[i][j][2] = 255
inv_test = cv2.bitwise_not(test)
with open('../foo.csv' , 'w' , newline = '') as f:
    thewriter = csv.writer(f)
    for i in range(len(x)):
        p = str(i) + ".jpg"
        img = cv2.imread(p)
        mask1 = np.resize(ellipMask , (700 , 700 , 3))
        mask1[0:350 , 0:350] = 255 , 255 , 255
        mask2 = np.resize(ellipMask , (700 , 700 , 3))
        mask2[0:350 , 350:700] = 255 , 255 , 255
        mask3 = np.resize(ellipMask , (700 , 700 , 3))
        mask3[350:700 , 0:350] = 255 , 255 , 255
        mask4 = np.resize(ellipMask , (700 , 700 , 3))
        mask4[350:700 , 350:700] = 255 , 255 , 255

        mask1 = cv2.bitwise_and(inv_test , mask1)
        mask2 = cv2.bitwise_and(inv_test , mask2)
        mask3 = cv2.bitwise_and(inv_test , mask3)
        mask4 = cv2.bitwise_and(inv_test , mask4)

        mask1 = cv2.bitwise_and(mask1 , img)
        mask2 = cv2.bitwise_and(mask2 , img)
        mask3 = cv2.bitwise_and(mask3 , img)
        mask4 = cv2.bitwise_and(mask4 , img)
        mask5 = cv2.bitwise_and(img , test)

        features = []

        color = ('b' , 'g' , 'r')
        for channel , col in enumerate(color):
            histr = cv2.calcHist([mask1] , [channel] , None , [64] , [1 , 255])
            features.extend(histr)
        for channel , col in enumerate(color):
            histr = cv2.calcHist([mask2] , [channel] , None , [64] , [1 , 255])
            features.extend(histr)
        for channel , col in enumerate(color):
            histr = cv2.calcHist([mask3] , [channel] , None , [64] , [1 , 255])
            features.extend(histr)
        for channel , col in enumerate(color):
            histr = cv2.calcHist([mask4] , [channel] , None , [64] , [1 , 255])
            features.extend(histr)
        for channel , col in enumerate(color):
            histr = cv2.calcHist([mask5] , [channel] , None , [64] , [1 , 255])
            features.extend(histr)
            
        gr = np.reshape(features , (1 , -1))
        thewriter.writerow(gr.tolist()[0])
