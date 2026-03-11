x = float(input("valor: "))
if(x<=300):
	valortotal=x+(0.1*x)
	print(round(valortotal,2))
else:
	valortotal=x+(0.06*x)
	print(round(valortotal,2))