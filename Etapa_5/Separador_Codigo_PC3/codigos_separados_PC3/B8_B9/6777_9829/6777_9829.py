ano = int(input("Digite o ano de nascimento: "))
pais = input("Digite o pais a ser analisado: ").upper()
idade = 2023 - ano

if pais == 'B':
	if idade >= 18:
		print("sim")
		print(idade - 18)
	elif idade < 18:
		print("nao")
		print(18 - idade)
elif pais == 'I':
	if idade >= 17:
		print("sim")
		print(idade)
	elif idade < 17:
		print("nao")
		print(17 - idade)
elif pais != 'B' and pais != 'I':
	print("invalido")