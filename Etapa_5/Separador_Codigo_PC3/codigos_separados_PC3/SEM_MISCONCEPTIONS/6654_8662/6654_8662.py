from numpy import *

pesos = array([1, 3, 2, 5])
notas = array(eval(input('Notas: ')))
soma = 0
somap = 0

for i in range(0, 4):
	soma = soma + pesos[i] * notas[i]
	somap = somap + pesos[i]

mediap = soma / somap

print(round(mediap, 2))