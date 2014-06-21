#proto.py

from __future__ import division
import numpy as np

import itertools
import argparse

from pyhull.delaunay import DelaunayTri


import matplotlib.pyplot as plt
import cv2
a=[]
img=cv2.imread('ball.jpg',0)
img = cv2.medianBlur(img,5) 
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,3,5)

for i in range (0,th2.shape[0]) :
        for j in range(0,th2.shape[1]):
                if th2[i,j]==0 :
                        a.append((j,i))





b=np.asarray(a)

for i in a :
        del i





dim =2


#for pt in b:
 #   p, = plt.plot(pt[0], pt[1], 'ro')
      





d = DelaunayTri(b)
del b
for s in d.simplices:
   for data in itertools.combinations(s.coords, dim):
        data = np.array(data)
        p, = plt.plot(data[:,0], data[:,1], 'g-')






for s in d.simplices:
    for data in itertools.combinations(s.coords, dim):
        data = np.array(data)
        p, = plt.plot(data[:,0], data[:,1], 'b-')
plt.imshow(cv2.Canny(img,200,200),cmap='gray')

plt.xticks([]), plt.yticks([])

plt.show()
