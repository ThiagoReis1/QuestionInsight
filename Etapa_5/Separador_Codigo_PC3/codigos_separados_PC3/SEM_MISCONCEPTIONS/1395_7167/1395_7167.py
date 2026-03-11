vendas = float(input("Insira um valor: "))

if (vendas <= 1000):
	comissao = vendas * 5/100
	print(round(comissao, 2))
else:
	comissao = (vendas * 10/100) - 1000*5/100
	print(round(comissao, 2))
	