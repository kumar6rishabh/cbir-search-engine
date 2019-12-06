import cv2
import numpy as np
import csv

img = cv2.imread(".//new_dataset//0.jpg")
img = cv2.GaussianBlur(img , (5 , 5) , 0)

#quantizing
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
with open('ccv_feat.csv' , 'w' , newline = '') as f:
    thewriter = csv.writer(f)
    for i in range(812):
        total = []
        path = "E:\\python37\\Image_processing\\cbir_system\\new_dataset\\"+str(i)+".jpg"
        img = cv2.imread(path)
        img = cv2.GaussianBlur(img , (5 , 5) , 0)
        rgb = cv2.split(img)
        q = []
        for ch in rgb:
            vf = np.vectorize(lambda x, div: int(x//div)*div)
            quantized = vf(ch, div)
            q.append(quantized.astype(np.uint8))
        img = cv2.merge(q)
        bgr = cv2.split(img)
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
        gr = np.reshape(total , (1 , -1))
        thewriter.writerow(gr.tolist()[0])
