ano = int(input("Digite o ano que voce nasceu:\n"))
pais = input("Digite o seu pais:\n")

pais = pais.upper()
idade = 2023 - ano
idadeB = 18
idadeJ = 16

if pais == "B":
	if idade >= idadeB:
		print("sim")
		print(idade - idadeB)
	else:
		print("nao")
		print(idadeB - idade)
elif pais == "J":
	if idade >= idadeJ:
		print("sim")
		print(idade - idadeJ)
	else:
		print("nao")
		print(idadeJ - idade)
else:
	print("invalido")