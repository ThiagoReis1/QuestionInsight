from numpy import *

v1 = array(eval(input("Informe as notas: ")))
pesos = [2,2,6,1]

peso_total = 0
soma = 0
i = 0
while (i < size(v1)):
	soma += v1[i] * pesos[i]
	peso_total += pesos[i]
	i += 1
	
media = soma / peso_total

print(round(media, 2))