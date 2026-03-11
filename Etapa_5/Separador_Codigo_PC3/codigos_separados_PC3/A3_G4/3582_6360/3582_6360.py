from numpy import *
v = array(eval(input()))

e = 0
i = 0
cont = 0
while i < size(v):
	if v[i] > 160:
		e = v[i] - 25
	else:
		e = v[i]
	cont = cont + e
	i = i + 1
print(round(cont, 2))