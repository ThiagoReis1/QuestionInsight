volume=float(input("De o valor de vendas: "))
if(volume<=1000):
	comissao=0.05*volume
	print(round(comissao,2))
else:
	comissao=(5/100)*1000+(10/100)*(volume-1000)
	print(round(comissao,2))