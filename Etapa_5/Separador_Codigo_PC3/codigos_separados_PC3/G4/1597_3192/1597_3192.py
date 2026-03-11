from numpy import * 

v = array(eval(input('compras: ')))

i = 0
soma = 0

while i < size(v):
	if (v[i] > 80):
		soma = soma + v[i] - 5
	else:
		soma = soma + v[i] 
	i = i + 1	

print(round(soma, 2))



		
	