valor = float(input("Insira o valor de venda: " ))

comissao_1 = valor * 0.05
comissao_2 = (0.05*1000.0) + (0.1*(valor-1000.0))

if valor <= 1000.0:
	print(round(comissao_1, 2))
	
else:
	print(round(comissao_2, 2))