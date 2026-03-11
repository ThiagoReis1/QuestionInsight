ano = int(input())
pais = input().upper()

if pais == "B":
	if (2023-ano) < 18:
		print("nao")
		print(18-(2023-ano))
	else:
		print("sim")
		print(0)
elif pais == "R":
	if (2023-ano) < 21:
		print("nao")
		print(21-(2023-ano))
	else:
		print("sim")
		print(0)
else:
	print("invalido")