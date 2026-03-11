from numpy import *
v = array(eval(input(": ")))
i = 0
j = 0
while i < size(v):
	if v[i] == 1:
		j += 100
	elif v[i] == 2:
		j += 60
	elif v[i] == 3:
		j += 20
	else:
		j += 0
	i +=1
print(j)