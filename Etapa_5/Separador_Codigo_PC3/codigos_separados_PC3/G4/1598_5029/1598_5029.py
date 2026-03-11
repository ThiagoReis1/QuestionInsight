from numpy import *

v = array(eval(input("")))

i = 0
a = 0

while (i < size(v)) :
	if (v[i] >= 90.0) :
		a = a + (v[i] - 6.50)
		i = i + 1
	else:
		a = a + v[i]
		i = i + 1
print(a)		
		