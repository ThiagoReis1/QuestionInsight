from numpy import *

v = array(eval(input("digite:")))
i = 0
acum = 0

while i < size(v):
	if v[i] == 1:
		ponto = 10
		acum += ponto
	elif v[i] == 2:
		acum += 5
	elif v[i] == 3:
		acum += 10
	elif v[i] == 4:
		acum += 5
	elif v[i] == 5:
		acum += 10
	elif v[i] == 6:
		acum += 5
	i += 1
	
print(acum)	