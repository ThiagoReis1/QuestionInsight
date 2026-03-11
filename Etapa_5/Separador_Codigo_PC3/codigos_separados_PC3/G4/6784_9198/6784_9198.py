x = int(input("Ano: "))
y = input("pais :").upper()

if y == "B":
	z = 2023 - x
	y = z - 21
	if z >= 21:
		print("sim")
		print(y)
	else:
		a = 21 - z
		print("nao")
		print(a)
elif y == "R":
	z = 2023 - x
	y = z - 18
	if z >= 18:
		print("sim")
		print(y)
	else:
		a = 18 - z
		print("nao")
		print(a)
else:
	print("invalido")