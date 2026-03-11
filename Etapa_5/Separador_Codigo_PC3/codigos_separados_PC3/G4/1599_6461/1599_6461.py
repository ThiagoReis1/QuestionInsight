from numpy import*

vet = array(eval(input("Vetor de custos: ")))

i = 0
item = 0
while size(vet) > i:
	if vet[i] >= 80.0:
		item = item * 0.015
print(round(item, 2))	