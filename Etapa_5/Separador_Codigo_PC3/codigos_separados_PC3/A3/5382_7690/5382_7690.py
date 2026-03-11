from numpy import*

marca = input()

i = 0
valor = 0
valora = 0
vogais = array(["A","E","I","O","U"])
j = 0

while(i < len(marca)):
	j = 0
	while(j<size(vogais)):
		if(marca[i] == vogais[j]):
			valor = valor + 0.25
		j = j + 1
	if(valor == valora):
		valor = valor + 0.27
	
	valora = valor
	i = i + 1
print(round(valor,2))