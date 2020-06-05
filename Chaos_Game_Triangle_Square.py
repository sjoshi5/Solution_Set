#Chaos Game for triangle and Square
#Changing the argument on line 27 toggles the triangle or square selection

import numpy
import matplotlib.pyplot as plt
import math
import random
#Calculate midpoint
def mid(a,b):
    return ((a[0]+b[0])/2, (a[1]+b[1])/2) 


n=int(input('No. of iterations:'))
x=numpy.zeros(n) #array for coordinates
y=numpy.zeros(n)
x[0]=random.random() #random selection of initial point
y[0]=random.random()
v=0
prev=5

#Set of vertices
vertex=[(0,0),(1,0),(0,1),(1,1)] 

for i in range(1,n):
        
    while(v==prev):
        v=random.randint(0,3) #randomise vertex index.
        #Second argument. 2:Triangle & 3:Square
    
    x[i],y[i]= mid(vertex[v],(x[i-1],y[i-1]))
    prev = v
plt.scatter(x,y)
plt.xlim(-0.5,1.5)
plt.ylim(-0.5,1.5)
plt.show()