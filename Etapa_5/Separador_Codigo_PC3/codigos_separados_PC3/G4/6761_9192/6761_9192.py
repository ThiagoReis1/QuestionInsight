Ib = float(input("Informe a velocidade da internet: "))

if Ib < 50:
	Tt = 60.00 + 4.50
	print(round(Tt,2))
	
elif Ib == 50:
	Tt = 60.00 + 5.50
	print(round(Tt,2))
	
else:
	Tt = 60.00 + 6.50
	print(round(Tt,2))