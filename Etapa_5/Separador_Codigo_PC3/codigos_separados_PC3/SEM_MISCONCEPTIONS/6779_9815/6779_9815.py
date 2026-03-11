nasci = int(input("Insira seu ano de nascimento: "))
pais = input("Em qual pais deseja verificar a idade minima: Japao (J) ou Brasil(B)").upper()

idade = 2023 - nasci

if pais == "B":
	if idade >= 18:
		print("sim")
		print(idade - 18)
	else:
		print("nao")
		print(18 - idade)
elif pais == "J":
	if idade >= 16:
		print("sim")
		print(idade - 16)
	else:
		print("nao")
		print(16 - idade)
else:
	print("invalido")
	