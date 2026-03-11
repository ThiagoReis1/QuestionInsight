ano = int(input())
pais = input()
pais = pais.upper()
idade = 2023 - ano
if pais == 'B' or pais == 'E':
	if pais == 'B':
		if idade >= 21:
			print('sim')
			print(idade - 21)
		else:
			print('nao')
			print(21 - idade)
	else:
		if idade >= 18:
			print('sim')
			print(idade - 18)
		else:
			print('nao')
			print(18 - idade)
else:
	print('invalido')