vendas = float(input("x: "))
mi = 1000
p1 = 5/100
p2 = 10/100

if (vendas >= mi):
	c = (vendas*p1)
else:
	exceder = float("valor excedido: ")
	c = (p1*mi)+(p2*(exceder-mi))
	
print(round(c, 2))