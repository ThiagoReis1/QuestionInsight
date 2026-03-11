# Entrada de variaveis
from numpy import*

valorcusto = array(eval(input("Quanto custa o produto: ")))
porcentagem = 0.15
i = 0
soma = 0

while i < size (valorcusto):
	
	if valorcusto[i] > 80:
		soma = soma + valorcusto[i] - (valorcusto[i] * porcentagem)
	else:
		soma = soma + valorcusto[i]

	i = i + 1
	
print(round(soma,2))