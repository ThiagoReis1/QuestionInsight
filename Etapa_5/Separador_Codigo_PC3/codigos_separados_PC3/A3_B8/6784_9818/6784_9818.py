ano = float(input("Ano de nascimento: "))
pais = input("B para Brasil e R para Reino Unido: ")
idade = 2023 - an

if pais == 'B' and idade >= 21:
	print("sim")
	print(idade - 21)
elif pais == 'B' and idade <= 21:
	print("nao")
	print(21 - idade)
elif pais == 'R' and idade >= 18:
	print("sim")
	print(idade - 18)
elif pais == 'R' and idade <= 18:
	print("nao")
	print(18 - idade)
elif pais != "B" or "R":
	print("invalido")