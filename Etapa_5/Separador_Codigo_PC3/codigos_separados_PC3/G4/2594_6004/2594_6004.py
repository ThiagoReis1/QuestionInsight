from numpy import *

d = array(eval(input()))
a=0

for i in range(len(d)):
	if ((d)[0] >= d[i]):
		a = a + d[i]
		
print(a)

		
	