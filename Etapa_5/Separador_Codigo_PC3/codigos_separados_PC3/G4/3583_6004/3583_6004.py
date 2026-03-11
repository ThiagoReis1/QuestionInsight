from numpy import *

c = array(eval(input()))
a=0

for i in range(len(c)):
	if (c[i] > 50.00):
		a = a + c[i] * 0.92
	else:
		a = a + c[i]
		
print(round(a, 2))