from numpy import * 
n = array(eval(input(" ")))
soma = 0
for x in n:
	if x == 88:
		soma = soma / 2
	else:
		soma = soma + x

print(soma)