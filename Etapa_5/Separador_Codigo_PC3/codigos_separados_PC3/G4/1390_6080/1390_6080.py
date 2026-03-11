con=float(input("consumo de minutos: "))


if (con<=100):
	var1=con*1.20
	
else:
	var1=con*1.40+25
print(round(var1, 2))
