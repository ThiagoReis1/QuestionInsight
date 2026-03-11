ano = int(input("Digite o ano de nascimento: "))
pais = str(input("Digite [B] para Brasil ou [E] para Estados Unidos: ")).upper()
idade = 2023 - ano

if pais == "B":
	if idade >= 21:
		print("sim")
		apta = 21 - idade
		print(apta)
	else:
		print("nao")
		apta = 21 - idade
		print(apta)
elif pais == "E":
	if idade >= 18:
		print("sim")
		apta = 18 - idade
		print(apta)
	else:
		print("nao")
		apta = 18 - idade
		print(apta)
else:
	print("invalido")
