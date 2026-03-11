ano = int(input())
p = input()

if p.upper()=='B':
	if 2023-ano < 21:
		print('nao')
		print(21-(2023-ano))
	else:
		print('sim')
		print((2023-ano)-21)
elif p.upper()=='R':
	if 2023-ano < 18:
		print('nao')
		print(18-(2023-ano))
	else:
		print('sim')
		print((2023-ano)-18)
else:
	print('invalido')