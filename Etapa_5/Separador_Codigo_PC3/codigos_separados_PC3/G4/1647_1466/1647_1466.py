from numpy import *
a=array(eval(input()))
b=zeros(size(a), dtype=int)
c=0
j=0
for i in range(size(a)):
	if(a[i]>=70):
		c+=1
		b[j]=i
		j+=1
d=zeros(j, dtype=int)
j=0
for k in range(size(d)):
	d[k]=b[j]
	j+=1
print(c)
print(d)
	
	