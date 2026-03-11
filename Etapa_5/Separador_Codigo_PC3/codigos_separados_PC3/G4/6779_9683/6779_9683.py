ano = int(input("Ano de nascimento:"))
pais = input("Coloque seu pais (B)rasil ou (J)apao:").upper()

if pais == "B":
	if ano >= 18:
		print("nao")
		a = 2023 - ano
		b = 18 - a
		print(b)
	else:
		print("sim")
		a = 2023 - ano
		b = 18 - a
		print (b)
elif pais == "J":
	if ano >= 16:
		print ("sim")
		a = 2023 - ano
		b = a - 16
		print(b)
	else:
		print("nao")
		a = 2023 - ano
		b = 16 - a
		print(b)
else:
	print("invalido")