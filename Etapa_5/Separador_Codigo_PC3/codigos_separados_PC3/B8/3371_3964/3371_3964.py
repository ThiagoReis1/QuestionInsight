unidade = input()
medida = float(input())

if unidade == 'M':
	km = 1.60934*medida
	print(round(km, 2))
	
elif unidade == 'K':
	mi = medida/1.60934
	print(round(mi, 2))