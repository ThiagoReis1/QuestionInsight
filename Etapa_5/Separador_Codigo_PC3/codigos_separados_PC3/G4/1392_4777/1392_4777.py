cons = float(input("valor do consumo: "))


if cons <= 10:
	vc = cons * 3 + 30
	print(round(vc, 2))
	
else: 
	vc = cons * 3.50 + 30
	print(round(vc, 2))