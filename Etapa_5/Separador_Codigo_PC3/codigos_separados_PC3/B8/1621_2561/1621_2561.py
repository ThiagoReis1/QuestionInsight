from numpy import *

nomes = array(eval(input("Digite os nomes dos produtos: ")))
quantidades = array(eval(input("Digite as quantidades dos produtos comprados: ")))

total = 0
i = 0
while (i < size(nomes)):
	if (nomes[i] == "ARROZ"):
		total = total + quantidades[i] * 1.25
	elif (nomes[i] == "FEIJAO"):
		total = total + quantidades[i] * 2.60
	elif (nomes[i] == "BIS"):
		total = total + quantidades[i] * 1.80
	elif (nomes[i] == "MIOJO"):
		total = total + quantidades[i] * 0.85
	elif (nomes[i] == "FANTA"):
		total = total + quantidades[i] * 3.20
	i = i + 1
print(round(total, 2))