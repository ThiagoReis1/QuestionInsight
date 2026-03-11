from numpy import *

c = array(eval(input("Compras: ")))

i=0
s=0
while i < size(c):
	if c[i] >= 80:
		c[i] = c[i]*0.85
	s=s+c[i]	
	i = i + 1
	
print(round(s,2))