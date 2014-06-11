#proto.py

from __future__ import division
import numpy as np

import itertools
import argparse

from pyhull.delaunay import DelaunayTri
from pyhull.convex_hull import ConvexHull

import matplotlib.pyplot as plt
import cv2
a=[]
img=cv2.imread('ball.jpg',0)
edges = cv2.Canny(img,100,200)
for i in range (0,200) :
        for j in range(0,200):
                if edges[i,j]==255 or (i%12==0 and i%20==0) :
                        a.append((j,i))





b=np.asarray(a)

legkeys = []

legitems = []
dim =2


#for pt in b:
 #   p, = plt.plot(pt[0], pt[1], 'ro')
      

#legkeys.append(p)
#comment out everything below this
legitems.append("Points")

d = DelaunayTri(b)

for s in d.simplices:
   for data in itertools.combinations(s.coords, dim):
        data = np.array(data)
        p, = plt.plot(data[:,0], data[:,1], 'g-')

legkeys.append(p)
legitems.append("Delaunay tri")

d = ConvexHull(b)

for s in d.simplices:
    for data in itertools.combinations(s.coords, dim):
        data = np.array(data)
        p, = plt.plot(data[:,0], data[:,1], 'b-')

legkeys.append(p)
legitems.append("Convex hull")
plt.xticks([]), plt.yticks([])

plt.show()
