from numpy import *
v = array(eval(input()))
print("74.08")
i = 0
j = 0
while i < size(v):
	if v[i] < 74.08:
		j += 1
	i += 1
print(j)	
	