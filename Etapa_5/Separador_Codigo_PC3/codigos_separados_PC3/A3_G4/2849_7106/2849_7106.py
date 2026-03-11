from numpy import *

v = array(eval(input()))
a = 0

for i in range (size(v)):
	if v[i] != 0:
		a = a + v[i]
	else:
		a = 0

	
print(a)
	
	
		

		