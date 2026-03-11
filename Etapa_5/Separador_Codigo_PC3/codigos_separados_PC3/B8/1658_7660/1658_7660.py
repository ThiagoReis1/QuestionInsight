#-------------------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 13/02/2023
# Objetivo: Contar a quantidade de pessoas de cada país.
#-------------------------------------------------------------------
from numpy import*

part = input("Defina os paises dos participantes: ")
part = part.upper()
paises = part.split(',')

qtd = zeros(5, dtype = int)
for i in range(size(paises)):
	# print (paises[i])
	if paises[i] == 'CHN':
		qtd[0] = qtd[0] + 1
	elif paises[i] == 'JPN':
		qtd[1] = qtd[1] + 1
	elif paises[i] == 'KOR':
		qtd[2] = qtd[2] + 1
	elif paises[i] == 'MGL':
		qtd[3] = qtd[3] + 1
	elif paises[i] == 'THA':
		qtd[4] = qtd[4] + 1
		
print (max(qtd))
print (qtd)