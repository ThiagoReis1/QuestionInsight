from numpy import *

notas = array(eval(input()))
pesos = array([3,5,1])

i = 0
numerador = 0
denominador = 0
total = 0

while i < size(notas):
	numerador += notas[i]*pesos[i]
	denominador += pesos[i]
	i += 1
total = numerador / denominador
print(round(total,2))
