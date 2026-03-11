from numpy import *
 
v = input()

p = 0
c = 0
while (p < len(v)):
	if (v[p] == "A" or v[p] == "E" or v[p] == "O" or v[p] == "I" or v[p] == "U"):
		c = c + 0.15
	else:
		c = c + 0.17
	p = p + 1

print(round(c,2))
