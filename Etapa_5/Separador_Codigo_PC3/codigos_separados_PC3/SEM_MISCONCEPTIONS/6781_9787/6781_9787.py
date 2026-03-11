ano = int(input("Idade: "))
pais = input("(B), (E): ").upper()
idade = 2023 - ano
if pais == "B":
	if idade >= 21:
		print("sim")
		print(idade - 21 )
	else:
		print("nao")
		print(21 - idade)

elif pais == "E":
	if idade >= 18:
		print("sim")
		print(idade - 18)
	else:
		print("nao")
		print(18 - idade)
else:
	print("invalido")
	