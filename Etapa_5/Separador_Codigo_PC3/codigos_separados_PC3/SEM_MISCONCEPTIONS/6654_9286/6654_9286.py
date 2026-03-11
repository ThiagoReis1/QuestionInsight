from numpy import *

notas = array(eval(input("Notas:")))
pesos = array([1,3,2,5])
den = sum(pesos)
i = 0
m = 0
while i < size(notas):
	m += notas[i]* pesos[i]
	i+=1

mp  =  m / den
print(round(mp,2))
