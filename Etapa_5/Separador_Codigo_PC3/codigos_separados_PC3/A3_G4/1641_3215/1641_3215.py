from numpy import *
v=array(eval(input()))
i=0

for x in v:
	if (x%3==0):
		i=i+1
print(i)
d=zeros(i,dtype=int)
b=0
c=0
for i in range(size(v)):	
	y=v[i]
	if (y%3==0):	
		d[b]=d[b]+i	
		b=b+1
		
print(d)

