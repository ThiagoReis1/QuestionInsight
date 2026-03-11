from numpy import *
v = array(eval(input("vetor de notas: ")))

i = 0

while i < size(v):
	if(v[i] >= 8):
		v[i] = 10
	if(v[i] <= 2):
		v[i] = 0
	else:
		v[i] = v[i]
	i = i + 1
print(v)		