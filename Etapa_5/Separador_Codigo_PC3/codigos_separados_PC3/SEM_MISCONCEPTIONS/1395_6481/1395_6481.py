vendas = float(input())

if vendas <= 1000:
	comissao = vendas*0.05
else:
	comissao = 1000*0.05 + (vendas - 1000)*0.10
print(round(comissao, 2))