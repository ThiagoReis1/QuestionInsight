ida = int(input("Ano de nascimento: "))
lc = input("Digite o local(B para Brasil e R para Reino unido): ").upper()

e = 2023 - ida

if lc == "B":

	if e >= 18:
		print("sim")
		print(e - 18)
	else:
		print("nao")
		print(18 - e)
		
elif lc == "R":

	if e >= 17:
		print("sim")
		print(e - 17)
	else:
		print("nao")
		print(17 - e)
	
else:
	print("invalido")