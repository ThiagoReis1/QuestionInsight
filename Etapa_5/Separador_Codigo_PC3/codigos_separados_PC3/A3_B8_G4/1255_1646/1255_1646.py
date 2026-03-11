from math import*
from numpy import*
v=array(eval(input()))
v1=array(2, dtype=int)
cont= 0
cont1= 0
for i in range (0 , size(v)):
	a= min("v")
	b= max("v")
c = (0.65 * a + 0.35 * b)
d = (0.45 * a + 0.55 * b)
for i in range (0 , size(v)):
	if(v[i]>= c and v[i] < d):
		v1[0]= v1[0]+1
	elif(v[i]>=d and v[i]< c) :
		v1[1]= v1[1]+1
print(v1)