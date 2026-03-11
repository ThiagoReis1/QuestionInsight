from numpy import *

v = array(eval(input("valor: ")))

i = 0
s = 0

while(i < size(v)):
	if(v[i] > 80.0):
		s = s + 1
		i = i + 1
	else:
		s = s
		i = i + 1

ss = s * 5
z = sum(v) - ss

print(round(z, 2))