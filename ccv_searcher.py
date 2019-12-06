import cv2
import numpy as np
import csv
import math

img = cv2.imread(".//new_dataset//250.jpg")
img = cv2.GaussianBlur(img , (5 , 5) , 0)

n = 64
div = 256//n #n is the number of bins, here n = 64
rgb = cv2.split(img)
q = []
for ch in rgb:
    vf = np.vectorize(lambda x, div: int(x//div)*div)
    quantized = vf(ch, div)
    q.append(quantized.astype(np.uint8))
img = cv2.merge(q)

row , col , channels = img.shape

connectivity = 8
tau = 0
if tau == 0:
    tau = row*col*0.1

rgb = cv2.split(img)
q = []
for ch in rgb:
    vf = np.vectorize(lambda x, div: int(x//div)*div)
    quantized = vf(ch, div)
    q.append(quantized.astype(np.uint8))
img = cv2.merge(q)
bgr = cv2.split(img)
total = []
for ch in bgr:
    for k in range(0 , 256 , div):
        temp = ch.copy()
        temp = (temp == k).astype(np.uint8)
        output = cv2.connectedComponentsWithStats(temp , connectivity , cv2.CV_32S)
        num_labels = output[0]
        labels = output[0]
        stats = output[2]
        centroids = output[3]
        alpha = 0
        beta = 0
        req = stats[1:]
        for r in req:
            if(r[4] >= tau):
                alpha += r[4]
            else:
                beta += r[4]
        total.append(alpha)
        total.append(beta)


dist = []
name = []
with open('ccv_feat.csv' , 'r') as csvFile:
    reader = csv.reader(csvFile)
    i = 0
    for row in reader:
        distance = math.sqrt(sum([(float(a) - float(b)) ** 2 for a , b in zip(row , total)]))
        dist.append(distance)
        nam = str(i)+".jpg"
        name.append(nam)
        i += 1

di = {}
for i in range(len(name)):
    di[name[i]] = dist[i]
sorted_di = sorted(di.items() , key = lambda kv : kv[1])

pic = []
t = 0
first_key = list(sorted_di)[:10]
for key , val in first_key:
    key = ".//new_dataset//"+key
    res = cv2.imread(key)
    na = str(t)
    cv2.imshow(na , res)
    t += 1
