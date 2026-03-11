valor = float(input('digite o valor da compra: '))
forma = input('forma de pagamento: (D/P/C1/C2)')

if (forma.upper() == 'D'):
	preco = valor - (valor * 12/100)
	print(round(preco, 2))
elif (forma.upper() == 'P'):
	preco = valor - (valor * 12/100)
	print(round(preco, 2))
elif (forma.upper() == 'C1'):
	preco = valor
	print(round(preco, 2))
elif (forma.upper() == 'C2'):
	preco = valor + (valor * 7/100)
	print(round(preco, 2))
else:
	print('utilize uma forma adequada')
	
