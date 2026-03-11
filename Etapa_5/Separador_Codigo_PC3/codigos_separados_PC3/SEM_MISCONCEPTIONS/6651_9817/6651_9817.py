from numpy import *
notas= array(eval(input("Insira um conj de notas:")))
pesos= array([5, 4, 3, 2])
i= 0
num= 0

while i < size(notas):
	num= num + (notas[i]* pesos[i])
	i= i + 1
	
media= num/sum(pesos)
print(round(media,2))