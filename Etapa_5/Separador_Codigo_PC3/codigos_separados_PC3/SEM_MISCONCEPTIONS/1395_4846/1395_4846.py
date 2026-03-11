vendas=float(input("Digite o volume de vendas:"))

if (vendas <= 1000):
	comissao=vendas*(5/100)
	print(round(vendas*5/100,2))

else:
	comissao = 1000*(5/100) +(vendas-1000)*(10/100)
	print(round(comissao,2))