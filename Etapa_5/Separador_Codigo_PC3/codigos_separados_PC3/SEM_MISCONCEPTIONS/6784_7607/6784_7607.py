nascimento = int(input("Qual o ano de nascimento da pessoa? "))
pais = input("Digite B para Brasil e R para Reino Unido: ").upper()

idade = 2023 - nascimento

if pais == "B" and idade >= 21:
	print("sim")
	apta = idade - 21
	print(apta)
elif pais =="B" and idade < 21:
	print("nao")
	faltam = 21 - idade
	print(faltam)
elif pais == "R" and idade >= 18:
	print("sim")
	apta = idade - 18
	print(apta)
elif pais == "R" and idade < 18:
	print("nao")
	faltam = 18 - idade
	print("nao")
else:
	print("invalido")