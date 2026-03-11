from numpy import *
v = array(eval(input()))

i = 0
d = 0

while i<size(v):
	if (v[i]>80):
		d = d + 5
	i = i + 1
ct = sum(v) - d

print(round(ct,2))