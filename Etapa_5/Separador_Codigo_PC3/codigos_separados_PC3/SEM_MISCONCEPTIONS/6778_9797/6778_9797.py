ano = int(input("Insira o ano de nascimento: "))
pais = input("Insira o pais: (B/J) ").upper()
idade = 2023 - ano

if pais == "B":
	if idade >= 21:
		print("sim")
		print(idade - 21)
	else:
		print("nao")
		print(21 - idade)
elif pais == "J":
	if	idade >= 20:
		print("sim")
		print(idade - 20)
	else:
		print("nao")
		print(20 - idade)
else:
	print("invalido")

	
	

