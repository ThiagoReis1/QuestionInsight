Ano = int(input("Ano de nascimento da pessoa: "))
Pais = input("De qual pais? B/E ").upper()
Idade = 2023 - Ano
IMpDB = 21
IMpDE = 18

if (Idade >= 21 and Pais == "B") or (Idade >= 18 and Pais == "E"):
	print("sim")
	if Pais == "B":
		print(Idade - IMpDB)
	else:
		print(Idade - IMpDE)
elif (Idade < 21 and Pais == "B") or (Idade < 18 and Pais == "E"):
	print("nao")
	if Pais == "B":
		print(IMpDB - Idade)
	else:
		print(IMpDE - Idade)
else:
	print("invalido")