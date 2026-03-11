from numpy import *
notas = array(eval(input('Notas: ')))
i = 0
soma = 0
p = 1
den = 0
while i < size(notas):
	soma = soma + notas[i] * p
	i = i + 1
	den = den + p
	p = p + 1
print(round(soma / den , 2))

	
	