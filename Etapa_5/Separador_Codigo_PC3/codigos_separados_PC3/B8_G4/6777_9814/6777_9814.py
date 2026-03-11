ano = int(input('Determine o ano de nascimento: '))
p = input('Escolha entre B e I: ').upper()

idade = 2023 - ano
tb = idade - 18
ti = idade - 17

if p != "B" and p != "I":
	print("invalido")
elif p == 'B':
	if idade >= 18:
		print('sim')
		print(tb)
	else:
		print('nao')
		print(-1 * tb)
elif p == 'I':
	if idade >= 17:
		print('sim')
		print(ti)
	else:
		print('nao')
		print(-1 * ti)