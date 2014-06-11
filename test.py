from __future__ import division
import numpy as np

import itertools
import argparse
import random

from pyhull.delaunay import DelaunayTri
from pyhull.convex_hull import ConvexHull
import matplotlib.pyplot as plt
import cv2
img=cv2.imread('lena.jpg',0)
points=np.zeros((10000,2))
temp=0
l=0
p=0
b=0
while(l<475):
	while(b<475):
		for i in range(l,l+24):
			for j in range(b,b+24):
				temp=temp+img[i,j]
		temp=temp/(900.0*500)
		temp=int(temp)
		x=l/25
		y=b/25
		for k in range(p,p+temp-1):
			points[k][0]=random.uniform(y,y+1)
			points[k][1]=random.uniform(x,x+1)
		p=p+temp
		temp=0
		b=b+25
	b=0
	l=l+25

for a in range(0,10000):
	print(points[a][0])
legkeys=[]
legitems=[]
dim=2
for pt in points:
    p, = plt.plot(pt[0], pt[1], 'ro')
      
'''
legkeys.append(p)
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
'''
plt.show()
