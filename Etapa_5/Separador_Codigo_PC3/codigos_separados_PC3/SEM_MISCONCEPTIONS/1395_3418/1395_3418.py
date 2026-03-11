#ENTRADA

valor_de_vendas = float(input("Valor de vendas: "))

#CONDICIONAL

if	(valor_de_vendas <= 1000.00):
	comissao = (valor_de_vendas*0.05)
else:
	dif = (valor_de_vendas - 1000.0)
	comissao = (1000.0*0.05) + (dif*0.1)
	
print(round(comissao,2))