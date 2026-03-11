from numpy import *
v = array(eval(input()))
cont = 10000
i = 0

while i < size(v):
	if v[i] == 1:
		cont = cont * 2
	elif v[i] == 2:
		cont = cont
	elif v[i] == 3:
		cont = cont / 2
	elif v[i] == 4:
		cont = cont / 4
	i += 1 
	
print(round(cont,2))