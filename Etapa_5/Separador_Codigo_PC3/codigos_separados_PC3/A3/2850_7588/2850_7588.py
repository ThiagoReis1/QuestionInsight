from numpy import *

h = array(eval(input()))

acum = 0
acumTotal = 0

for i in range(size(h)):
	acum += h[i]
	if(acum >= 55):
		acum = 0
	acumTotal += acum

print(acum)