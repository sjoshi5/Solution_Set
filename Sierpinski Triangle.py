#Chaos Game: Sierpinski Triangle 
#Considering Equilateral Triangle

import numpy
import matplotlib.pyplot as plt
import math
import random
#Calculating midpoint
def mid(a,b):
    return ((a[0]+b[0])/2, (a[1]+b[1])/2) 

n = int(input('No. of iterations:'))
x=numpy.zeros(n) #array for coordinates
y=numpy.zeros(n)
x[0]=random.random() #random selection of initial point
y[0]=random.random()

vertex=[(0,0),(2, math.sqrt(3)),(4,0)] #Equilateral triangle

for i in range(1,n):
    v=random.randint(0,2) #randomise vertex index
    x[i],y[i]= mid(vertex[v],(x[i-1],y[i-1]))

plt.scatter(x,y)
plt.show()

