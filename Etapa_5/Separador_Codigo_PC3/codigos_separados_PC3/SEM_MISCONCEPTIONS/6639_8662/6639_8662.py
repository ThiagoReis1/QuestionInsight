texto = input('Digite algo: ').upper()
cont = 0

if 'M' not in texto:
	print('nao achei')
else:
	for i in texto:
		if i == 'M':
			print((cont))
		cont = cont + 1