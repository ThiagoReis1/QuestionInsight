Dt = int(input("digite o ano de nascimento: "))
Ps = input("Em que pais o sujeito nasceu? ").upper()

Id = 2023 - Dt

if Ps == "B":
	if Id >= 21:
		print("sim")
		print(Id - 21)
	elif Id <= 21:
		print("nao")
		print(21 - Id)
if Ps == "E":
	if Id >= 18:
		print("sim")
		print(Id - 18)
	elif Id <= 18:
		print("nao")
		print(18 - Id)
elif Ps != "B" and "E":
	print("invalido")