ano = int(input("Digite o ano de nascimento: "))
pais = input("Digite 'B' para Brasil e 'C' para China: ").upper()

idade = 2023 - ano

if (idade>= 21 and pais == 'B'):
	print("sim")
	apta = idade - 21
	print(apta)
	
elif (idade<21 and pais == 'B'):
	print("nao")
	apta = 21 - idade
	print(apta)
	
elif (idade>= 24 and pais == 'C'):
	print("sim")
	apta = idade - 24
	print(apta)
	
elif (idade<24 and pais == 'C'):
	print("nao")
	apta = 24 - idade
	print(apta)
	
elif (pais!='B' and pais!='C'):
	print("invalido")