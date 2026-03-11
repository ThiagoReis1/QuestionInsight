ano = int(input("ano: "))
pais = str(input("pais: ")).upper()
###########################
if pais not in ("B","I"):
	print("invalido")
if (2023 - ano >= 18) and (pais == "B"):
	print("sim")
	resto = (2023 - ano) - 18
	print(resto)
else:
	if (2023 - ano < 18) and pais == "B":
		print("nao")
		resto = 18 - (2023 - ano)
		print(resto)
	else:
		if (2023 - ano >= 17) and pais == "I":
			print("sim")
			resto = (2023 - ano) - 17
			print(resto)
		else:
			if (2023 - ano < 17) and pais == "I":
				print("nao")
				resto = 17 - (2023 - ano)
				print(resto)
