from numpy import *
v = array(eval(input()))
i = 0
j = 0
while i < size(v):
	if v[i] < -100:
		j += 1
	i += 1	
v1 = array(ones(size(v) - j,dtype=float))
i = 0
j = 0
while j < size(v):
	if v[j] >= -100:
		v1[i] = v[j]
		i += 1
	j += 1	
print(v1)	