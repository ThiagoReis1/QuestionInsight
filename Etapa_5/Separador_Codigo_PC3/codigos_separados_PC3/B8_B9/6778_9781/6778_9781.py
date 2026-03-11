ano = int(input())
pais_origem = input().upper()
ar = (2023 - ano)
if pais_origem =="B":
	if ar >= 21:
		print("sim")
		print(round(ar - 21, 2))
	elif ar < 21:
		print("nao")
		print(round(21 - ar, 2))
elif pais_origem == "J":
	if ar >= 20:
		print("sim")
		print(round(ar - 20, 2))
	elif ar < 20:
		print("nao")
		print(round(20 - ar, 2))
	else:
		print("invalido")
	