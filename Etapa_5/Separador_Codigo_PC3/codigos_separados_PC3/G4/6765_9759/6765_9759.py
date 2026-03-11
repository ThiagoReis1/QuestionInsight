ano = int(input("Informe o ano de nascimento: "))
pais = input("Informe B para Brasil ou R para Russia: ").upper()


x = 2023 - ano 

if pais == "B":
	if x >= 18: 
		print("sim")
		print(x - 18)
	else:
		print("nao")
		print(18 - x)
elif pais == "R":
	if x >= 21:
		print("sim")
		print(x - 21)
	else: 
		print("nao")
		print(21 - x)
else:
	print("invalido")