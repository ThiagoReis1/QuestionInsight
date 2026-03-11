from numpy import *

z = (zeros,4(dtype=int))
var = array(input('')).upper().split(',')

for i in var:
	if var == 'A':
		z[0] += 1
	elif var == 'B':
		z[1] += 1
	elif var == 'C':
		z[2] += 1
	elif var == 'D':
		z[3] += 1

print(var)