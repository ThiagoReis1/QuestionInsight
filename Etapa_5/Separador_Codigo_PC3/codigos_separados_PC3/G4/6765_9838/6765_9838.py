ano = int(input("Ano nascimento: "))
pais = input("Pais (B ou R): ")

if pais.upper() == 'B':
	tot = 2023 - ano
	if tot >= 18:
		print("sim")
		print(tot-18)
	else:
		print("nao")
		print(18-tot)
elif pais.upper() == 'R':
	tot = 2023 - ano
	if tot >= 21:
		print("sim")
		print(tot-21)
	else:
		print("nao")
		print(21-tot)
else:
	print("invalido")