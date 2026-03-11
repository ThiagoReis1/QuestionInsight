vendas = float(input("Digite o valor do volume de vendas: "))

e = (vendas - 1000)
c1 = vendas*5/100
c2 = 1000*5/100 + (e*10/100)

if(vendas <= 1000):
	print(round(c1, 2))
else:
	print(round(c2, 2))