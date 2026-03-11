from numpy import *

pesos = array([4, 3])

notas = array(eval(input(" : ")))

i = 0
num = 0
den = sum(pesos)
while i < size(pesos) :
	num += notas[i]*pesos[i]
	i += 1
print(round(num/den, 2))