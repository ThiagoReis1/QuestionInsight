from numpy import *

notas = array(eval(input("insira:")))
pesos = array([3,5,1])

i= 0
num = 0

while i < size(notas):
	num += notas[i] * pesos[i]
	i +=1
	
media = num/sum(pesos)
print(round(media, 2))
	
		
						 