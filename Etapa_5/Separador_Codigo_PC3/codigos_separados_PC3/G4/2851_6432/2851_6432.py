from numpy import *

x = array(eval(input("")))


acum = 0

for i in range(size(x)):
	if x[i] == 99:
		acum = acum * 2
	else:
		acum = acum + x[i]
print(acum)