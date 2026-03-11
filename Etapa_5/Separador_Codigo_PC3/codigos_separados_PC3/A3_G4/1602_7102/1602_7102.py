from numpy import *

v = array(eval(input()))
i=0
j = 0

if(v[i] > v[i+1]):
	j = i
else:
	j = i + 1
	
print(j)