numero = int(input())

if numero % 47 == 0:
	print(numero // 47)
	print('sim')
else:
	print(numero % 47)
	print('nao')