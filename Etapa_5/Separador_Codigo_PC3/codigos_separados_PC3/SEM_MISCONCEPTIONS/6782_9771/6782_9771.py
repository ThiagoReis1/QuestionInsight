ano = int(input())
pais = input()
pais = pais.upper()
idade = 2023 - ano
if pais == "B" or pais == "E":
	if pais == "B":
		if idade >= 18:
			print("sim")
			print(idade - 18)
		else:
			print("nao")
			print(18 - idade)
	else:
		if idade >= 16:
			print("sim")
			print(idade - 16)
		else:
			print("nao")
			print(16 - idade)
else:
	print("invalido")