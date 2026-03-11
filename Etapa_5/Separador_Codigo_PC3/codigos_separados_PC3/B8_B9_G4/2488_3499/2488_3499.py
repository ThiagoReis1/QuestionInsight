a = float(input('salario atual:'))
print('Entrada: R$', a )

if (a > 0):
	if(a <= 800):
		x = (50/100)* a + a
		print('Novo salario: R$', round(x, 2))
	elif((a > 800) and (a <= 1000)):
		x = (40/100)* a + a
		print('Novo salario: R$', round(x, 2))
	elif((a > 1000) and (a <= 1200)):
		x = (30/100)* a + a
		print('Novo salario: R$', round(x, 2))
	elif((a > 1200) and (a <= 1400)):
		x = (20/100)* a + a
		print('Novo salario: R$', round(x, 2))
	elif((a > 1400) and (a <= 1600)):
		x = (10/100)* a + a
		print('Novo salario: R$', round(x, 2))
	elif(a > 1600):
		x = (5/100)* a + a
		print('Novo salario: R$', round(x, 2))
else:
	print('Dado invalido')
		
		  
		