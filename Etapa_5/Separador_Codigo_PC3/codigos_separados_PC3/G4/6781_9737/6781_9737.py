ano = int(input("Nascimento: "))
pais = input("B ou E: ").upper()

idd = 2023 - ano
aptB = 21 - idd
aptE = 18 - idd

if pais == "B":
	if idd >= 21:
		print("sim")
		print(aptB)
	else:
		print("nao")
		print(aptB)
elif pais == "E":
	if idd >= 18:
		print("sim")
		print(aptE)
	else:
		print("nao")
		print(aptE)
else:
	print("invalido")