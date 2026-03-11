from numpy import *

n = array(eval(input("")))

a = 0

for i in n :
	if (i == 10) :
		a = a * i
	else:
		a = a + i
print(a)		
		