from numpy import *
v=array(eval(input()))
n=array([3,5,1])
i=0
while i < size(v):
	s=sum((v*n)/9)
	i+=1
print(round(s,2))