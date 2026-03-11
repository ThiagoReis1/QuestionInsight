city = input()
age = int(input())
print("Entradas: ", city, ",", age)
if(city == "Porto Velho"):
	valor = 500
	if(age <= 2 and age >=0):
		print("Passagem: R$ 0,00")
	elif(3 <= age and age <=12):
		valor = valor/2
		print("Passagem: R$", round(valor, 2))
	elif(13 <= age and age < 65):
		print("Passagem: R$", round(valor, 2))
	elif(age >= 65):
		valor = valor - (valor * 0.3)
		print("Passagem: R$", round(valor, 2))
	else:
		print("entradas invalidas")
elif(city == "Santerem"):
	valor = 370
	if(age <= 2 and age >=0):
		print("Passagem: R$ 0,00")
	elif(3 <= age and age <=12):
		valor = valor/2
		print("Passagem: R$", round(valor, 2))
	elif(13 <= age and age < 65):
		print("Passagem: R$", round(valor, 2))
	elif(age >= 65):
		valor = valor - (valor * 0.3)
		print("Passagem: R$", round(valor, 2))
	else:
		print("entradas invalidas")
elif(city == "Belem"):
	valor = 600
	if(age <= 2 and age >=0):
		print("Passagem: R$ 0,00")
	elif(3 <= age and age <=12):
		valor = valor/2
		print("Passagem: R$", round(valor, 2))
	elif(13 <= age and age < 65):
		print("Passagem: R$", round(valor, 2))
	elif(age >= 65):
		valor = valor - (valor * 0.3)
		print("Passagem: R$", round(valor, 2))
	else:
		print("entradas invalidas")
elif(city == "Tefe"):
	valor = 360
	if(age <= 2 and age >=0):
		print("Passagem: R$ 0,00")
	elif(3 <= age and age <=12):
		valor = valor/2
		print("Passagem: R$", round(valor, 2))
	elif(13 <= age and age < 65):
		print("Passagem: R$", round(valor, 2))
	elif(age >= 65):
		valor = valor - (valor * 0.3)
		print("Passagem: R$", round(valor, 2))
	else:
		print("entradas invalidas")
elif(city == "Tabatinga"):
	valor = 550
	if(age <= 2 and age >=0):
		print("Passagem: R$ 0,00")
	elif(3 <= age and age <=12):
		valor = valor/2
		print("Passagem: R$", round(valor, 2))
	elif(13 <= age and age < 65):
		print("Passagem: R$", round(valor, 2))
	elif(age >= 65):
		valor = valor - (valor * 0.3)
		print("Passagem: R$", round(valor, 2))
	else:
		print("entradas invalidas")
else:
	print("entradas invalidas")
	