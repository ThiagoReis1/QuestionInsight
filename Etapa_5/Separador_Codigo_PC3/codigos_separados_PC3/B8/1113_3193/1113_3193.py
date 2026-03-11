idade = int(input('idade:'))
peso = float(input('peso:'))
print('Entradas:', idade, 'anos e', peso, 'kg')
if(idade > 0 and idade< 130 and peso > 0.0 and peso < 550.0):
	if(idade <= 20 and peso <= 60):
		x = '9'
		print('Grupo de risco:', x)
	elif(idade <= 20 and (peso > 60 and peso <= 90)):
		x = '8'
		print('Grupo de risco:', x)
	elif(idade <= 20 and peso > 90):
		x = '7'
		print('Grupo de risco:', x)
	elif((idade > 20 and idade <= 50) and peso < 60):
		x = '6'
		print('Grupo de risco:', x)
	elif((idade > 20 and idade <= 50) and (peso > 60 and peso <= 90)):
		x = '5'
		print('Grupo de risco:', x)
	elif((idade > 20 and idade <= 50) and peso > 90):
		x = '4'
		print('Grupo de risco:', x)
	elif(idade > 50 and peso < 60):
		x = '3'
		print('Grupo de risco:', x)
	elif(idade > 50 and peso > 60 and peso <= 90):
		x = '2'
		print('Grupo de risco:', x)
	elif(idade > 50 and peso > 90):
		x = '1'
		print('Grupo de risco:', x)
else:
	print('Dados invalidos')