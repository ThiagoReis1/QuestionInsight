valor_de_vendas=float(input("valor de venda"))
excedente=valor_de_vendas-1000
if(valor_de_vendas<=1000):
	comissao=valor_de_vendas*5/100
	print(round(comissao,2))
else:
	comissao=1000*5/100+excedente*10/100
	print(round(comissao,2))