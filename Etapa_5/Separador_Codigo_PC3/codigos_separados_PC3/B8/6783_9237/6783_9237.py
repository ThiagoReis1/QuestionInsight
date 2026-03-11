nasc = int(input("ano de nascimento: "))
pais = input("Brasil ou stados Unidos: ")

idade = (2023 - nasc)
if (pais.upper() == "B") or (pais.upper() == "E"):
	if (pais.upper() == "B"):
		anos = (idade - 18)
		anos_f = (18 - idade)
		if (idade >= 18):
			print("sim")
			print(anos)
		else:
			print("nao")
			print(anos_f)
	elif (pais.upper() == "E"):
		anos = (idade - 16)
		anos_f = (16 - idade)
		if (idade >=  16):
			print("sim")
			print(anos)
		else:
			print("nao")
			print(anos_f)
else:
	print("invalido")