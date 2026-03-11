year = int(input("Ano de nascimento: "))
country = input("Brasil ou Japao? ").upper()

if (country == "B"):
	i = 2023 - year
	if (i >= 18):
		print("sim")
		print(i)
	else:
		i = 2023 - year
		n = 18 - i
		print("nao")
		print(n)
elif (country == "J"):
	i = 2023 - year
	n = i - 16
	if (i >= 16):
		print("sim")
		print(n)
	else: 
		print("nao")
		print(n)
else:
	print("invalido")
