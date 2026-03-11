ano = int(input("Ano de nascimento: "))
pais = input("[B]rasil / [C]hina: ").upper()
idade = 2023 - ano

if (idade >= 21) and (pais == "B"):
	print("sim")
	print(2002 - ano)
	
elif (idade >= 24) and (pais == "C"):
	print("sim")
	print(1999 - ano)
	
elif (idade < 21) and (pais == "B"):
	print("nao")
	print(21 - idade)
	
elif (idade < 24) and (pais == "C"):
	print("nao")
	print(24 - idade)
	
elif (pais != "C") or (pais != "B"):
	print("invalido")