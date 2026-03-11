from numpy import *

v = array(eval(input("")))

i = 0

while i < size(v):
	if v[i] < 2:
		v[i] = v[i] * 0
	elif v[i] > 8:
		v[i] = 10
	i = i + 1
print(v)