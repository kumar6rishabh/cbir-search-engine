import numpy as np
import math
import cv2
import os
import csv
import operator

os.chdir('./new_dataset')
image = input("Enter the picture ")
img = cv2.imread(image+".jpg")

img = cv2.resize(img , (700 , 700))

k = list(img.shape)
h = k[0]
w = k[1]
ellipMask = np.zeros((700 , 700) , dtype = "uint8")
new_ellipMask = np.resize(ellipMask , (700 , 700 , 3))
mask1 = np.resize(ellipMask , (700 , 700 , 3))
mask1[0:350 , 0:350] = 255 , 255 , 255
mask2 = np.resize(ellipMask , (700 , 700 , 3))
mask2[0:350 , 350:700] = 255 , 255 , 255
mask3 = np.resize(ellipMask , (700 , 700 , 3))
mask3[350:700 , 0:350] = 255 , 255 , 255
mask4 = np.resize(ellipMask , (700 , 700 , 3))
mask4[350:700 , 350:700] = 255 , 255 , 255
test = cv2.ellipse(new_ellipMask , (350 , 350) , (200 , 150) , 0 , 0 , 360 , 255 , -1)
for i in range(700):
    for j in range(700):
        if(test[i][j][0] != 0):
            test[i][j][0] = 255
            test[i][j][1] = 255
            test[i][j][2] = 255


inv_test = cv2.bitwise_not(test)
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

'''addr = []
for i in range(len(features)):
    addr.append(float(features[i]))
print(addr)'''


dist = []
name = []
with open('../foo.csv' , 'r') as csvFile:
    reader = csv.reader(csvFile)
    i = 0
    for row in reader:
        distance = math.sqrt(sum([(float(a) - float(b)) ** 2 for a , b in zip(row , features)]))
        dist.append(distance)
        nam = str(i)+".jpg"
        name.append(nam)
        i += 1

di = {}
for i in range(len(name)):
    di[name[i]] = dist[i]
sorted_di = sorted(di.items() , key = lambda kv : kv[1])
#print(sorted_di)
#print("hi")
pic = []
t = 0
first_key = list(sorted_di)[:10]
for key , val in first_key:
    res = cv2.imread(key)
    na = str(t)
    cv2.imshow(na , res)
    t += 1
