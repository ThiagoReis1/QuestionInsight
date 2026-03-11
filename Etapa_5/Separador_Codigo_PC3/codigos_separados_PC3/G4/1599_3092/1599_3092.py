from numpy import *

v = array(eval(input("v?")))
p=0
i=0

while (i< size(v)):
	if (v[i] > 80):
		p=v[i]*0.85+p
	else:
		p=p+v[i]
	i=i+1
	
print(round(p,2))