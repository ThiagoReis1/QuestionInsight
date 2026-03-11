string = input("digite a sequencia:")

valor_mercearia = 7.25
valor_padaria = 4.75
valor_rotisseria = 3.50

total_compra = 0.0
quantidade_mercearia = 0
quantidade_padaria = 0
quantidade_rotisseria = 0

for produto in string:
	if produto == "M":
		total_compra += valor_mercearia
		quantidade_mercearia += 1
	elif produto == "P":
		total_compra += valor_padaria
		quantidade_padaria += 1
	elif produto == "R":
		total_compra += valor_rotisseria
		quantidade_rotisseria += 1

total_compra = round(total_compra, 2)

output = ("{ :.2f} - {} - {} - {}")
print(output.format(total_compra, quantidade_mercearia, quantidade_padaria, quantidade_rotisseria))
		