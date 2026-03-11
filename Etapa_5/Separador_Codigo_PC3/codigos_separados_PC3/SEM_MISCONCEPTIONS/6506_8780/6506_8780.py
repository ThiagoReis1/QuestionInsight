#Entrada

qtde_pratos = int(input("Digite a quantidade de pratos: "))
escolha = input("Sobremesa? (S/N) ")

#Expressão e Saída

if escolha.upper() == "S":
	total = (40 * qtde_pratos) - (qtde_pratos * 40) * 5 / 100
	print(round(total, 2))
else:
	total = 40 * qtde_pratos
	print(round(total, 2))