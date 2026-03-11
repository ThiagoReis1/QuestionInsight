valordevendas=float(input("valor de vendas realizadas:"))

if(valordevendas<=1000):
	comissao=5/100 * valordevendas
	print(round(comissao,2))
else:
	bonus=(valordevendas-1000)*10/100
	comissao=5/100*1000 + bonus
	print(round(comissao,2))