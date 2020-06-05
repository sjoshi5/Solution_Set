import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#AGM Function 
def AGM(x,y):
    a=x
    g=y
    while(abs(a-g) > 1.e-10): #Allowed error for limiting iterations
        a=((x+y)/2)
        g=(math.sqrt(x*y))
        x=a
        y=g
    return(a)


L = int(input('Lower limit for range:'))
U = int(input('Upper limit for range:'))
n = U-L+1

#For 3D plot of numbers against AGM 
fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
X=[]
Y=[]
#Set of numbers on X and Y axes
for i in range(L,U+1):
    for j in range (0,n):
        X.append(i)

for i in range(0,n):
    for j in range(L,U+1):
        Y.append(j)

#Creating the resultant AGM 
res = []
for i in range(L,U+1):
    for j in range(L,U+1):
        res.append(AGM(i,j))

#Plots of Results
ax.scatter(X,Y,res)
ax.set_xlabel('Range of Numbers')
ax.set_ylabel('Range of Numbers')
ax.set_zlabel('Value of AGM')
plt.show()

