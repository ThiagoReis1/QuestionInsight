ano = int(input())
pais = input().upper()

sobra = 24 - (2023-ano)

if pais == "C":
	a = 2023 - ano
	if a >= 24:
		print("sim")
		print(a-24)
	else:
		print("nao")
		x = 24 - (2023-ano)
		print(x)
elif pais == "B":
	a = 2023 - ano
	if a >=21:
		print("sim")
		print(a-21)
	else:
		print("nao")
		x = 21 - (2023-ano)
		print(x)
else:
	print("invalido")