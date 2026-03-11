from numpy import *

v=array(eval(input()))

for i in range(size(v)):
	if v[i]!=7:
		v[i]=v[i]**2
	else:
		v[i]=49
print(v)