from numpy import *
v=array(eval(input("")))

for i in range(size(v)):
	v[i]=(v[i]+1)**3
	if v[i]==1000:
		v[i]=0
print(v)
	
	