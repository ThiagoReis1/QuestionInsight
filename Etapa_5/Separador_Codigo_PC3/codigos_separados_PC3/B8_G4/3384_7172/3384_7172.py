med=input("O para oncas ou K para quilogramas: ")

if(med.upper()=="K"):
	Kg=float(input("para quilogramas: "))
	Oz=35.274*Kg
	print(round(Oz, 2))
else:
	if(med.upper()=="O"):
		Oz=float(input("para oncas: "))
		Kg=Oz/35.274
		print(round(Kg, 2))