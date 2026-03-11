nascimento = int(input("Ano nascimento: "))
pais = input("B para brasil e J para japao: ").upper()

idade = 2023 - nascimento 

if pais == "B" and idade < 21:
	print("nao")
	print(21 - idade)
elif pais == "B" and idade > 21:
	print("sim")
	print(idade - 21)
elif pais == "J" and idade < 20:
	print("nao")
	print(20 - idade)
elif pais == "J" and idade > 20:
	print("sim")
	print(idade - 20)