venda=float(input("qual valor de vendas?"))
if(0<venda<=1000):
	comissao=(0.05*venda)
	print(round(comissao,2))
else:
	comissao=(0.05*1000)+(0.10*(venda-1000))
	print(round(comissao,2))