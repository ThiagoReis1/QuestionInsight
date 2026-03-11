n = int(input())
p = input()
p = p.upper()
ida = 2023 - n
if p == 'B':
	idaminima = 21
	if ida >=idaminima:
		print('sim')
		print(idaminima - ida)
	else:
		print('nao')
		print(idaminima%ida)
elif p == 'E':
	idaminima = 18
	if ida>=idaminima:
		print('sim')
		print(idaminima - ida)
	else:
		print('nao')
		print(idaminima%ida)
else:
	print('invalido')
	