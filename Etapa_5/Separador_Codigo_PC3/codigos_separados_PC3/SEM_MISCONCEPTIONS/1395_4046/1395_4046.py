
vendas = float(input("Informe o valor das vendas: "))

if(vendas <= 1000):
	comissao = (vendas * (5 / 100))
else:
	comissao = ((1000 * (5 / 100) + (vendas - 1000) * (10 / 100)))

print(round(comissao, 2))