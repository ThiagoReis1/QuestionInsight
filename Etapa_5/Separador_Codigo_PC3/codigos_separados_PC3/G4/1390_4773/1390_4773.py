cons = float(input("minutos consumidos: "))

if cons <= 100:
	print(round(cons*1.20, 2))
else: 
	print(round(cons*1.40 + 25, 2))