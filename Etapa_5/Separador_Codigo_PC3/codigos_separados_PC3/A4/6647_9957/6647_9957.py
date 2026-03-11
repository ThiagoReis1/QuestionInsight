from numpy import *
notas = array(eval(input()))

pesos = [2,1,5]
						 
notas = notas * pesos

media = sum(notas) / sum(pesos)

round = round(media, 2)
print(round)
