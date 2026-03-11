from numpy import *

v = array(eval(input()))
i=0
t = min(v)

while (i < size(v)):
	
	if (v[i] == t):
		
		a = i
		
	i = i + 1
print(a)