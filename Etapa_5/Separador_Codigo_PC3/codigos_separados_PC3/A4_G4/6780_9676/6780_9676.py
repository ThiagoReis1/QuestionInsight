ano = int(input("ano de nascimento"))
pais = input("B para Brasil e C para China")

if pais.upper() == "B":
	min = 2023 - ano
	if min < 21:
		print("nao")
		print(21 - min)
	else:
		print("sim")
		print(min - 21)
elif pais.upper() == "C":
	min = 2023 - ano
	if min < 24:
		print("nao")
		print(24 - min)
	else:
		print("sim")
		print(min-24)
else:
	print("invalido")
		