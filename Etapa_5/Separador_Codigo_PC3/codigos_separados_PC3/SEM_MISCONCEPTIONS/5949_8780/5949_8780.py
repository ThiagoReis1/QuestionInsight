#Entrada

escolha = input("Fatia de bolo ou Croissant? (B/C) ")
qtde_comida = int(input("Quantidade de comida: "))
qtde_cap = int(input("Quantidade de Cappuccinos: "))

#Expressão e Saída

if escolha.upper() == "B":
	total = qtde_comida * 3 + qtde_cap * 5.5
	print(round(total, 2))
else:
	total = qtde_comida * 6 + qtde_cap * 5.5
	print(round(total, 2))