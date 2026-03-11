from numpy import *
andares = array(eval(input()))
tam = size(andares)
i = 0
soma = 0

while tam > (i + 1):
	d = (andares[i+1] - andares[i])
	if d > 0:
		soma = soma + d 
		i = i + 1
	else: 
		soma = soma + (d *(-1))
		i = i +1
print(soma * 3)
	