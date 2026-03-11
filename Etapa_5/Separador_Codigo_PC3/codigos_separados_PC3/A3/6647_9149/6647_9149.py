from numpy import * 

notas = array(eval(input('')))
pesos = array([2,1,5])

i = 0
num = 0
den = 0
total = 0

while i < size(notas):
	num += notas[i] * pesos[i]
	den += pesos[i]
	i += 1
	
total = num / den

print(round(total, 2))