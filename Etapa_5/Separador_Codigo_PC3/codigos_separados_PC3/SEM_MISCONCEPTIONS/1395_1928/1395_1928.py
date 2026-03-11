vendas = float(input("Informe vendas: "))
comissao1 = vendas * 0.05
comissao2 = comissao1 * 0.10

if (vendas > 1000.0):
	pagamento = comissao2
	print(round(comissao2,2)