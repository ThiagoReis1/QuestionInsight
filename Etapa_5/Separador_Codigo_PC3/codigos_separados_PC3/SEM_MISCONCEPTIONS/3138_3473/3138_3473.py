vet = eval(input())
aux = 0
for i in vet:
	aux = aux + i**7
aux = aux/len(vet)

saida = aux ** (1/7)

print(round(saida,2))