from numpy import *
from numpy.linalg import *
t= array(eval(input()))
a=0
for c in t:
	if(c%5==0):
		a+=1
v=zeros(a,dtype=int)
a2=0
for c in range(size(t)):
	if(t[c]%5==0):
		v[a2]=c
		a2+=1
print(a)
print(v)

