venda = float(input("Volume de Vendas: "))
if(venda<=1000):
	print(round(venda*0.05,2))
else:
   print(round(1000*0.05+((venda-1000)*0.10),2))