from numpy import *

notas = array(eval(input('notasd dos alunos: ')))
pesos = array([2, 2, 6, 1])

i = 0 #indice
num = 0 #acumulador do numerador

while i < size(notas):
	num += notas[i] * pesos[i]
	i += 1
	
media = num / sum(pesos)
print(round(media, 2))