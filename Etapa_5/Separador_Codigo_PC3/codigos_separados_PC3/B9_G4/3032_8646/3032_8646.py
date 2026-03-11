from math import *

p = (float(input()))

if p <= 0:
	op = 0
	
elif (p > 0) and (p<= 1):
	op = 1
	
elif (p > 1) and (p <= 2):
	op = (p**0.5)

else:
	op = (p**(1/3))
	
print(round(op, 4))

