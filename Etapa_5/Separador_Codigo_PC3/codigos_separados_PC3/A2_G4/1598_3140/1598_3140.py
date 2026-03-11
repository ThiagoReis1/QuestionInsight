from numpy import*
from numpy.linalg import*

v = array(eval(input("")))
s = sum(v)
for i in range(size(v)):
	if(v[i]>80):
		s=s-5
	else:
		s=s	
print(round(s,2))
	