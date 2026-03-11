ar = input("Qual o nome da armadura? ")
fd = int(input("Qual o fator de destreza? "))


if(ar == "malha"):
	malha = 15 * fd - 1
	print(malha)
else:
	placa = 20 * fd - 18
	print(placa)
