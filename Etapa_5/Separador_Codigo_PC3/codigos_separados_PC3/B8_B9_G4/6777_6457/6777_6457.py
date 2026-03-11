nas = int(input("Digite o ano de nascimento:"))
pais = input("Digite o pais: ").upper()

if pais == "B":
	x = 2023 - nas
	if x >= 18:
		y = x - 18
		print("sim")
		print(y)
	elif x < 18:
		y = 18 - x
		print("nao")
		print(y)
elif pais == "I":
	x = 2023 - nas
	if x >= 17:
		y = x - 17
		print("sim")
		print(y)
	elif x < 17:
		y = 17 - x
		print("nao")
		print(y)
else:
	print("invalido")