from numpy import *

n = eval(input("lista:"))
i = 0
p =0
d = 0
while i < size(n):
	if n[i] >= 40:
		d += 1
	p = p + n[i]
	i = i + 1
	
print(round(p - (2.50 * d),2))