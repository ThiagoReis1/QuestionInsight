valor_peso = float(input("valor: "))
valor_fixo = 10.0

if valor_peso < 5:
	taxa = 3.75
	custo = (valor_fixo + taxa)
elif valor_peso == 5:
	taxa = 4.75
	custo = (valor_fixo + taxa)
else:
	taxa = 5.75
	custo = (valor_fixo + taxa)
valor_total = valor_peso * valor_fixo

print(round(custo, 2))