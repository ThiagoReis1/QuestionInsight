n = int(input("Ano de nascimento: "))
pais = input("Pais que deseja dirigir B (Brasil) ou E (EUA): ").upper()

idade = 2023 - n

if pais == "B":
	if idade >= 18:
		apta = idade - 18
		print("sim")
		print(apta)
	
	else:
		nao = 18 - idade
		print("nao")
		print(nao)
		
elif pais == "E":
	if idade >= 16:
		apta2 = idade - 16
		print("sim")
		print(apta2)
		
	else:
		nao2 = 16 - idade
		print("nao")
		print(nao2)

else:
	print("invalido")