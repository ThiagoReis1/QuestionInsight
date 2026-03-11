from numpy import *

v = array(eval(input("v: ")))

i = 0

while i < size(v):
	if v[i] > 4 and v[i] < 5:
		v[i] = 4
	elif v[i] < 10 and v[i] > 9:
		v[i] = 10
	i = i + 1
	
print(v)