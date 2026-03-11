from numpy import*
from math import*
vetor=array(eval(input("Notas : ")))
cont = 0
tamanho = size(vetor)
menornota = min(vetor)
soma = sum(vetor)
while(cont<tamanho):
	if(vetor[cont] == menornota):
		soma = soma - min(vetor)
		cont = cont - 1
	else:
		cont = cont + 1
media = soma/cont
print(round(media,2))