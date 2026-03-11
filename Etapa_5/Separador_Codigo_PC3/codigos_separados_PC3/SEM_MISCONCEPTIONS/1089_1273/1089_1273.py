valor_compra_1 = float(input())
valor_compra_2 = float(input())
valor_compra_3 = float(input())
limite_cartao_de_credito = float(input())

total_das_compras = valor_compra_1 + valor_compra_2 + valor_compra_3

print(round(total_das_compras, 2))
if (total_das_compras <= limite_cartao_de_credito):
	print("Sim")
else:
	print("Nao")