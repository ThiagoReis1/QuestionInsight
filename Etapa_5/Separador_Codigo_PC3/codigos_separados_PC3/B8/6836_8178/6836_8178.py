from numpy import*

preco_bebida = 6.80
preco_congelado = 11.75
preco_mercearia = 5.90

entrada = input("digite a sequencia de prudutos: ")

total = 0
i = 0

while i < len(entrada):
	produto = entrada[i]
	if produto == "B":
		total += preco_bebida
	elif produto == "C":
		total += preco_congelado
	elif produto == "M":
		total += preco_mercearia
	i += 1
		
preco_total = round(total,2)
print(preco_total)