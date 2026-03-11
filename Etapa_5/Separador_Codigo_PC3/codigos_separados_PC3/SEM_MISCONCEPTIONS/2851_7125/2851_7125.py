from numpy import*

elementos = array(eval(input(": ")))
soma = 0

for x in elementos:
	if x == 99:
		soma = soma * 2
	else:
		soma = soma + x
print(soma)