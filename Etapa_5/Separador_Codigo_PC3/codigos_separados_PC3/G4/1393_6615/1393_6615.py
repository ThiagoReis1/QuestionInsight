P = float(input("digite o peso das encomendas: "))
TT1 = (P * 0.05)
TT2 = (P * 0.04) + 60.00
if (P < 5000):	
	print(round(TT1,2))
else:	
	print(round(TT2,2))