from numpy import * 

notas = array(eval(input("insira as notas: ")))
pesos = array([5, 4, 3, 2])

den = sum(pesos)
num = 0
i = 0

while	i < size(notas):
	num += notas[i] * pesos[i]
	i += 1
	
mp = num / den
print(round(mp, 2))