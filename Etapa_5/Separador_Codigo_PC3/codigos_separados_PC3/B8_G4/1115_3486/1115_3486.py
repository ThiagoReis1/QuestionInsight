sa = float(input('salario atual:'))
cod = int(input('digite o codigo:'))
print('Entradas: R$ ', sa, 'e codigo',cod)
if(sa>0)and(cod==101)or(cod==102)or(cod==103)or(cod==104):
	if(cod==101):
		x = ((0.80*sa)/100)+sa
		print('Novo salario: R$ ',round(x, 2))
	elif(cod==102):
		x = ((0.65*sa)/100)+sa
		print('Novo salario: R$ ',round(x, 2))
	elif(cod==103):
		x = ((0.60*sa)/100)+sa
		print('Novo salario: R$ ',round(x, 2))
	elif(cod==104):
		x = ((0.55*sa)/100)+sa
		print('Novo salario: R$ ',round(x, 2))
else:
	print('Dados invalidos')