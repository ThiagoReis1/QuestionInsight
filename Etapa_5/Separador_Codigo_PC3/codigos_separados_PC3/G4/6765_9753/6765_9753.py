n = int(input("ano de nascimento:"))
pais = input("pais:")
if pais.upper() == "B":
	if (2023 - n >=18):
		print("sim")
		print((2023- n)- 18)
	else:
		print("nao")
		print(18 -(2023 -n))
elif pais.upper() == "R":
	if (2023 - n) >=21:
		print("sim")
		print((2023 - n)- 21)
	else:
		print("nao")
		print(18 - (2023 - n))
else:
	print("invalido")