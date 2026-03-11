from numpy import *
v = array(eval(input()))

e = 0
i = 0
cont = 0
while i < size(v):
	if v[i] == 1:
		e = 100
	elif v[i] == 2:
		e = 60
	elif v[i] == 3:
		e = 20
	elif v[i] == 4:
		e = 0
	cont = cont + e
	e = 0
	i = i + 1
print(cont)