N = int(input())
pais = input().upper()

if	pais == 'B':
	if	2023 - N >= 21:
		print('sim')
		print(2023-N-21)
	else:
		print('nao')
		print(21-(2023-N))
elif	pais == 'R':
	if	2023 - N >= 18:
		print('sim')
		print(2023-N-18)
	else:
		print('nao')
		print(18-(2023-N))
else:
	print('invalido')