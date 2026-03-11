ano = int(input("ano de nascimento: "))
pais = input("B para Brasil e R se Russia: ").upper()

i = (ano - 2023)

if pais == "B" and i >= 18:
	print("sim")
	print(i - 18)
elif pais == "R" and i >= 21:
	print("nao")
	i = (2023 - ano)
	print(21 - i)
else:
	print("invalido")