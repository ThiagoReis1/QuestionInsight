ano = int(input("ano: "))
pais = input("pais: ").upper()
idade = (2023 - ano)
if pais == 'B':
	if idade >= 18:
		print("sim")
		print( idade - 18)
	else:
		print("nao")
		print(18 - idade)
if pais == 'R':
	if idade >= 17:
		print("sim")
		print( idade - 17)
	else:
		print("nao")
		print(17 - idade)