nasc = int(input("Digite o seu ano de nascimento: "))
pais = input("Insira B para Brasil e C para China: ").upper()
idade = 2023 - nasc

if pais == "B":
	if idade >= 21:
		print("sim")
		print(idade - 21)
	else:
		print("nao")
		print(21 - idade)
		
elif pais == "C":
	if idade >= 24:
		print("sim")
		print(idade - 24)
	else:
		print("nao")
		print(24 - idade)

else:
	print("invalido")
	