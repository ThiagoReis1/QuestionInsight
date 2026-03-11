from numpy import *

notas = array(eval(input(" ")))
pesos = array ([2,1,5])
tamanho = sum(pesos)
num = 0
i = 0

while i < size(notas):
	num += notas[i] * pesos[i]
	i += 1

media_ponderada = num/tamanho
print(round(media_ponderada,2))