compra = float(input(''))
pagamento = input('')

desconto1 = 0.13
juros = 0.08

if pagamento == 'C' :
	quantas = int(input(''))
	if quantas == 1 :
		final = compra
	else:
		final = compra +(compra * juros)
elif pagamento == 'D' or pagamento =='P' :
	final = compra - (compra * desconto1)
	
	
print(round(final,2))
	

	