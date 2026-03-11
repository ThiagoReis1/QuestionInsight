from numpy import *

custo = array(eval(input("valor de cada item comprado:")))

i = 0 #posicao
acum = 0

while i < size(custo):
	if custo[i] > 80:
		desc = custo[i] * (15/100)	
		acum = acum + desc
	i = i + 1
		
	
	
total = 	sum(custo) - acum

print(round(total, 2))

