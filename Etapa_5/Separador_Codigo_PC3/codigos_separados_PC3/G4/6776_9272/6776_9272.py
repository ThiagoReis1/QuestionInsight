ano = int(input("ano de nascimento:"))
ps = input("digite b para brasil e r para reino unido:").upper()
x = 2023 - ano
if ps == "B":
	if x >= 18:
		print("sim")
		y = (2023 - ano) - 18
		print(y)
	else:
		print("nao")
		y = 18 - (2023 - ano)
		print(y)
elif ps == "R":
	if x >= 17:
		print("sim")
		y = (2023 - ano) - 17
		print(y)
	else:
		print("nao")
		y = 17 - (2023 - ano)
else:
	print("invalido")
