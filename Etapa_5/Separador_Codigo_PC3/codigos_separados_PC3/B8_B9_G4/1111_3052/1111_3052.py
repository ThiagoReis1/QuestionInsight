E= float (input ('Numero de horas extras: '))
F= float (input ('Numero de horas nao trabalhadas: '))
print ('Entradas:',E,'horas extras e',F,'horas de falta')

H= (E - (2 * F)/3)

if (E < 0) or (F < 0):
	print ('Dados invalidos')
	
elif (E > 0) and (F > 0):
	if (H > 2400):
		G= 500.00
	elif (H > 1800) and (H <= 2400):
		G= 400.00
	elif (H > 1200) and (H <= 1800):
		G= 300.00
	elif (H > 600) and (H <= 1200):
		G= 200.00
	elif (H <= 600):
		G= 100.00
	print ('Gratificacao: R$',round (G,2))