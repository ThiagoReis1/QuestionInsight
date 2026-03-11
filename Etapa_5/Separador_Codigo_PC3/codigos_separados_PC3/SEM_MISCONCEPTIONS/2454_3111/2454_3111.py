Altura = float(input("Altura em metros "))
Sexo = str.upper(input("Sexo M/F"))

if((Altura < 1) and (Altura > 2.5)):
	print("altura invalida")
elif(Sexo != "M" and  Sexo != "F"):
	print("codigo invalido de sexo")
else:
	if(Sexo == "M"):
		print(round((72.7*Altura)-58.2))
	elif(Sexo == "F"):
		print(round((62.1*Altura)-44.7.2))