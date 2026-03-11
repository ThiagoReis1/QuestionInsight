from numpy import *

v=array(eval(input("Digite aqui o vetor:")))
v1=zeros(2,dtype=int)
a=min(v)
b=max(v)
c=0.6*a+0.4*b
d=0.3*a+0.7*b
for i in range(0,size(v)):
	if(v[i]>=c and v[i]<d):
		v1[0]=v1[0]+1
	elif(v[i]>=d and v[i]<b):
		v1[1]=v1[1]+1
print(v1)