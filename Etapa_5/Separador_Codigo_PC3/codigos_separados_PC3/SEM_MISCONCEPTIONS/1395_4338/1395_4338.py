comissao1 = 0.05 #5%
comissao2 = 50 #mais 4.0 por valor excedente a 1000.00

vendas = float(input("Vendas em real: "))

if(vendas <= 1000):
	comissao = (vendas * comissao1)
else:
	comissao = (comissao2 + ((vendas - 1000) * 0.1))
print(round(comissao, 2))