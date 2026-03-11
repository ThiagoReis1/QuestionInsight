vendas = float(input("Digite o valor das vendas: "))

if(vendas <= 1000):
	comissao = (5/100) * vendas
else:
	comissao = (5/100) * 1000 + (1/10) * (vendas - 1000)
	
print(round(comissao, 2))