from numpy import *

v = array(eval(input()))
s = 0

for i in range(0, size(v)):
	
	if(v[i] == 99):
		
		s = s * 2
		i = i + 1
		
	else:
		
		s = s + v[i] 
	
print(s)