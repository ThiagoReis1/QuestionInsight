p = input('Determine a satisfacao: ').upper()

cont = 0

if p == 'X' or p == 'S' or p == 'N' or p == ' I':
	while p != 'X':
		if p == 'S':
			cont += 1
		p = input('determine a nova satisfacao: ').upper()
	print(cont)
else:
	print('nao fuja da pesquisa')