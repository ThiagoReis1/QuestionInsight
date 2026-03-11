v = float(input("Valor de vendas: "))
if(v <= 1000):
	c = (5/100)*v
	print(round(c,2))
else:
	e = v - 1000
	c = (5/100)*1000+10/100*e
	print(round(c,2))
	