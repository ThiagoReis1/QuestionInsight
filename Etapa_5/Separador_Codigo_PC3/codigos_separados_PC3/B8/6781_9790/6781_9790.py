nascimento = int(input("ano de nascimento: "))
pais = input("pais: ").upper()

if pais == 'B':
	if nascimento <= 2002:
		print("sim")
		diferenca = (2023 - nascimento)-21
		print( diferenca)
	elif nascimento >= 2002:
		print("nao")
		diferenca = 21-(2023 - nascimento)
		print(diferenca)
elif pais == 'E':
	if nascimento <= 2005:
		print("sim")
		diferenca = (2023 - nascimento)-18
		print(diferenca)
	elif nascimento >= 2005:
		print("nao")
		diferenca = 18-(2023 - nascimento)
		print(diferenca)
else:
	print("invalido")