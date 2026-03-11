from numpy import *

v=array(eval(input()))
d=zeros(size(v),dtype=float)
p=0
for i in range (size(v)):
	if v[i]>(c):
		d[i]+=1
	p+=1
	else:
		print (0.0)
print(d)

	