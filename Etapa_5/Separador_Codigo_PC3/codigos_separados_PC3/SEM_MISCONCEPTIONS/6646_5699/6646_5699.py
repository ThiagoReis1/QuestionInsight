from numpy import *

vetor = array(eval(input()))
pesos = [1,2,3]
soma = 0

i = 0
while i < 3:
	soma += (vetor[i]*pesos[i])
	i+=1

media = soma / 6
print(round(media,2))