arm = input('informe o nome da armadura, malha/placas: ').lower()
dest = int(input('informe o valor da destreza: '))

if arm == 'malha':
	res = 15 * dest - 1
	print(res)
else:
	res = 20 * dest - 18
	print(res)
	