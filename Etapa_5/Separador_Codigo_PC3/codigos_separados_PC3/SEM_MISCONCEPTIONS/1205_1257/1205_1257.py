# Mayara Soares
# 11 - 08 - 2016
# Av. 05   Ex. 01

from numpy import*

vetor_distancias = array(eval(input("Digite as distâncias obtidas: ")))
recorde = 8.95
print(recorde)
i = 0
j = 0

while (i < size(vetor_distancias)):
	if (vetor_distancias[i] > recorde):
		j = j + 1
	i = i + 1
	
print(j)


