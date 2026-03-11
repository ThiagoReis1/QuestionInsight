from numpy import *

v = array(eval(input()))
c=0
for i in range(size(v)):
	if v[i]>=5: 
		c+=1
ap=zeros(c, dtype=int)
j=0
for i in range(size(v)):
	if v[i]>=5:
		ap[j]=i
		j+=1
print(c)
print(ap)