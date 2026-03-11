compra = float(input('valor da compra'))
cod = input('codigo')

if(cod.upper() == 'D'):
	valor = compra - (compra * 12/100)
	print(round(valor, 2))
	
elif(cod.upper() == 'P'):
	valor = compra - (compra * 12/100)
	print(round(valor, 2))
	
elif(cod.upper() == 'C1'):
	valor = compra
	print(round(valor, 2))
	
elif(cod.upper() == 'C2'):
	valor = compra + (compra * 7/100)
	print(round(valor, 2))
	
else:
	print('use uma forma valida')
