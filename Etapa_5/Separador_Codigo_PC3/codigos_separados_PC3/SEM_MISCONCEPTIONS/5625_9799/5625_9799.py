intens = input('T ou S')
quantidade = int(input(''))
quantidade_acai = int(input(''))

if intens =='T':
	valor = (quantidade * 5.50) + (quantidade_acai * 10.0)
	print(round(valor,2))
else:
	valor = (quantidade * 4.00) + (quantidade_acai * 10.0)
	print(round(valor,2))
	
	