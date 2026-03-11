nascimento = int(input())
pais = input()

idade = 2023 - nascimento

if pais.upper() == "B":
	if idade >=18:
		print("sim")
		print(idade - 18)
	else:
		print("nao")
		print(18 - idade)
elif pais.upper() == "R":
	if idade >= 21:
		print("sim")
		print(idade - 21)
	else:
		print("nao")
		print(21 - idade)
else:
	print("invalido")