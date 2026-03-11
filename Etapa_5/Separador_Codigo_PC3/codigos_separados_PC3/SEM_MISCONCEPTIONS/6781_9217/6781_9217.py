birth = int(input("Ano de nascimento: "))
pais = str(input("Brasil ou Estados unidos (B ou E): ")).lower()

idade = 2023 - birth

if pais == "b":
	if idade >= 21:
		
		print("sim")
		print(idade - 21)
		
	else:
		print("nao")
		print(21 - idade)
		
elif pais == "e":
	if idade >= 18:
		
		print("sim")
		print(idade - 18)
		
	else:
		print("nao")
		print( 18 - idade)
		
else:
	print("invalido")
	

		