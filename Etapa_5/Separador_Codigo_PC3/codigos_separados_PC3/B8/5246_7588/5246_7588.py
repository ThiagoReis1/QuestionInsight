idade = int(input())
weight = float(input())

if(130 > idade > 0) and (550 > weight > 0):
	if(idade <= 20) and (weight <= 60):
		print('Grupo de risco: 9')
	elif(idade <= 20) and (90 >= weight > 60):
		print('Grupo de risco: 8')
	elif(idade <= 20) and (weight > 90):
		print('Grupo de risco: 7')
	elif(50 >= idade > 20) and (weight <= 60):
		print('Grupo de risco: 6')
	elif(50 >= idade > 20) and (90 >= weight > 60):
		print('Grupo de risco: 5')
	elif(50 >= idade > 20) and (weight > 90):
		print('Grupo de risco: 4')
	elif(idade > 50) and (weight <= 60):
		print('Grupo de risco: 3')
	elif(idade > 50) and (90 >= weight > 60):
		print('Grupo de risco: 2')
	elif(idade > 50) and (weight > 90):
		print('Grupo de risco: 1')
else:
	print('Dados invalidos')