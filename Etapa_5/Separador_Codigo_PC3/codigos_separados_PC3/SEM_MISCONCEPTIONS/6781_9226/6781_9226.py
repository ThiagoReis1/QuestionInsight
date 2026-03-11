ano = int(input("digite o ano de nascimento: "))
pais = input("digite o pais desejado: ")
idade = 2023 - ano

if pais.upper() == "B" and idade >= 21:
	print("sim")
	apto = idade - 21
	print(apto)
elif pais.upper() == "B" and idade < 21:
	print("nao")
	naoapto = 21 - idade
	print(naoapto)
elif pais.upper() == "E" and idade >= 18:
	print("sim")
	apto = idade - 18
	print(apto)
elif pais.upper() == "E" and idade < 18:
	print("nao")
	naoapto = idade + 18
	print(naoapto)
else:
	print("invalido")
	
