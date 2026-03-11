ano = int(input("insira seu ano de nascimento: "))
pais = input("insira o pais em que deseja verificar a idade minima (B/I): ").upper()

idade = 2023 - ano


if pais == "B" and idade >= 18:
	print("sim")
	sobra = idade - 18
	print(sobra)
	
elif pais == "B" and idade < 18:
	print("nao")
	falta = 18 - idade
	print(falta)
	
elif pais == "I" and idade >= 17:
	print("sim")
	sobra = idade - 17
	print(sobra)

elif pais == "I" and idade < 17:
	print("nao")
	falta = 17 - idade
	print(falta)