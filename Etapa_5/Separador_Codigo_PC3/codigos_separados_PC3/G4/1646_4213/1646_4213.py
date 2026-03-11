from numpy import *
a=array(eval(input("Saques:")))
b=size(a)
m=0
for i in range(b):
	if(a[i]<=50):
		m=m+1
v=zeros(m, dtype=int)
k=0
for i in range(b):
	if(a[i]<=50):
		v[k]=i
		k=k+1
print(m)
print(v)