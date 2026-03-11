from numpy import *

produto=eval(input("digite o valor do produto: "))

i = 0
soma = 0
while i < size(produto):
	if produto[i] > 50:
		soma=soma + (produto[i] - (produto[i] * 0.08))
	else:
		soma = soma + produto[i]
	i= i + 1
print(round(soma,2))