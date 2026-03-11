opcao = str(input())

if opcao == 'T':
	quant_fatias = int(input())
	quant_cap = int(input())
	conta = (quant_fatias * 6.0) + (quant_cap * 4.5)
	print(round(conta, 2))
else:
	if opcao == 'P':
		quant_pasteis = int(input())
		quant_cap = int(input())
		conta = (quant_pasteis * 5.0) + (quant_cap * 4.5)
		print(round(conta, 2))