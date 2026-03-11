x = float(input("n real: "))
k = int(input("k termos: "))

csh = 0
i = 0
from math import *
while (i<k):
	par = (2*i)
	denom = factorial(par)
	numer = x**(par)
	csh = (numer/denom)+csh
	i = i + 1
print(round(csh,8))