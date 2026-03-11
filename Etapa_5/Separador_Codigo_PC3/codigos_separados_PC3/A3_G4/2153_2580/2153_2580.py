from math import*
from numpy import*
x=array(eval(input("vetor1: ")))
y=array(eval(input("vetor2: ")))
z=zeros(x,dtype=float)
w=zeros(y,dtype=float)
i=0
for i in range (x):
	for j in range (y):
		d=(sqrt((x[i]-y[j])**2))
print(round(d,4))