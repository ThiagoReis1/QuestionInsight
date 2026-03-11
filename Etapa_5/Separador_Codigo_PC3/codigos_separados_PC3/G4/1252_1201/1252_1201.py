from numpy import *
v=array(eval(input()))
b=(max(v))
a=(min(v))
c= 0.6*a + 0.4*b
d= 0.3*a + 0.7*b
x=zeros(2,dtype=int)

for i in range(0,size(v)):
	if (v[i]>=a)and(v[i]<c):
		x[0]=x[0]+1
	if (v[i]>=c)and(v[i]<d):
		x[1]=x[1]+1
print(x)
	
