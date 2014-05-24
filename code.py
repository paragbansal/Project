
from __future__ import division
import numpy as np

import itertools
import argparse

from pyhull.delaunay import DelaunayTri
from pyhull.convex_hull import ConvexHull
import matplotlib.pyplot as plt
import cv2
img=cv2.imread('lena.jpg',0)
temp=0
for i in range(10,16):
	temp= img[i,i]+temp
temp=temp/6
temp=temp/15
temp=int (temp)
points=np.random.randn(temp,2)

legkeys = []
legitems = []
dim =2


#for pt in points:
    #p, = plt.plot(pt[0], pt[1], 'ro')
      

#legkeys.append(p)
legitems.append("Points")

d = DelaunayTri(points)

for s in d.simplices:
    for data in itertools.combinations(s.coords, dim):
        data = np.array(data)
        p, = plt.plot(data[:,0], data[:,1], 'g-')

legkeys.append(p)
legitems.append("Delaunay tri")

d = ConvexHull(points)

for s in d.simplices:
    for data in itertools.combinations(s.coords, dim):
        data = np.array(data)
        p, = plt.plot(data[:,0], data[:,1], 'b-')

legkeys.append(p)
legitems.append("Convex hull")

plt.show()
