m = input("digite a medida desejada: (M/K)")
k = float(input("digite um valor para medida: "))

if m.upper() == "M":
	mg = k/2.35215
	print(round(mg,2))
	
else:
	mg = k*2.35215
	print(round(mg,2))