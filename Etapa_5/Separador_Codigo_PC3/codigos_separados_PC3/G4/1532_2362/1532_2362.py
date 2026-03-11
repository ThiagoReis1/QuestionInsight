from math import *
x = float(input(":"))
k = int(input(":"))

va = 0
vc = 1

while(k > 0):
	k = k-1
	va = va + x**vc/factorial(vc)
	vc = vc + 2
print(round(va,9))	
