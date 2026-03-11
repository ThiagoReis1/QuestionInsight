cor = input('Leia cor:')
soma = 0
while cor.upper() != 'S':
	if cor.upper() == 'PRETA':
		soma += 1
	cor = input('Leia cor:')
print(soma)	
		