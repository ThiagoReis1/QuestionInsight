from numpy import *
v = array(eval(input("> ")))
L = len(v)

for i in range(L):
	v[i] = v[i]*2
print(v)