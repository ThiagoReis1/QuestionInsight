produto = input("Digite o nome do produto: ").upper()
i = 0
cont = 0
while i < len(produto):
	if produto[i] == "C":
		cont += 10.50
	elif produto[i] == "E":
		cont += 8.75
	elif produto[i] == "P":
		cont += 17.90
	i += 1
print(round(cont, 2))