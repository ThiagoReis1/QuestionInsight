valor_de_vendas = float(input(" Digite um numero: "))
valor_de_comissao = float( valor_de_vendas + 0.05)


if (valor_de_vendas <= 1.000):
	x = (valor_de_comissao)
	print(round(x,2))
			
else:
	y = (valor_de_vendas + 0.1)
	print(round(y,2))