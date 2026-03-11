from numpy import *

entrada = array(eval(input()))
pesos = [5,4,3,2]
nota = 0
for i in range(size(entrada)):
	nota += entrada[i] * pesos[i]
	
notaFinal = nota / sum(pesos)
print(round(notaFinal,2))

