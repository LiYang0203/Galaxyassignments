#!/usr/bin/env python
import csv
import numpy as np

with open('Abell2255.csv') as csvfile:
#	for row in islice(csvfile,1,None):
	reader=csv.reader(csvfile)
	for i,row in enumerate(reader):
		if i > 2:
			col=[row[9] for row in reader]
#	col[0]='0.0'
new=[]
for n in col:
	new.append(float(n))
col=new
#print(col)
with open('Abell2255.csv') as csvfile:
	reader1=csv.reader(csvfile)
	for i,row in enumerate(reader1):
		if i > 2:
			col1=[row[10] for row in reader1]
new1=[]
for n in col1:
	new1.append(float(n))
col1=new1
#print(col1)
a = np.array(col)
b = np.array(col1)
xx = a - b
#print(xx)

with open('Abell2255.csv') as csvfile:
	reader2=csv.reader(csvfile)
	for i,row in enumerate(reader2):
		if i > 2:
			col2=[row[10] for row in reader2]
new2=[]
for n in col2:
	new2.append(float(n))
col2=new2
#print(col1)
with open('Abell2255.csv') as csvfile:
	reader3=csv.reader(csvfile)
	for i,row in enumerate(reader3):
		if i > 2:
			col3=[row[11] for row in reader3]
new3=[]
for n in col3:
	new3.append(float(n))
col3=new3
c = np.array(col2)
d = np.array(col3)
yy = c - d
#print(yy)

import matplotlib.pyplot as plt
plt.title('color of galaxies in cluster')
plt.xlabel('u-g magnitude')
plt.ylabel('g-r magnitude')
plt.plot(xx,yy,'bo')
x=np.linspace(-6,8)
y=-x+2.2
plt.plot(x,y,color='red',linewidth=2)
plt.show()