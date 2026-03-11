year = int(input("digite um year: "))
contry = input("digite B para Brasil e R para Reino Unido: ").upper()

idade = 2023 - year
if contry == "R":
	if idade >= 18:
		print("sim")
		idade = (2023 -  year)-18
		print(idade)
	else:
		print("nao")
		idade = 18 - (2023 - year)
		print(idade)
elif contry == "B":
	if idade >=21:
		print("sim")
		idade =(2023 - year) - 21
		print(idade)
	else:
		print("nao")
		idade = 21 - (2023 - year)
		print(idade)
else:
 print("invalido")