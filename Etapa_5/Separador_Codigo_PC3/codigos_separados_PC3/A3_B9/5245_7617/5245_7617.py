salario = float(input('Digite o salario atual: '))

total = 0
valido = True

if (salario < 0):
	valido = False
elif (salario <= 800):
	porcentagem = salario * (50/100)
	total = salario + porcentagem
elif (salario > 800 and salario <= 1000):
	porcentagem = salario * (40/100)
	total = salario + porcentagem
elif (salario > 1000 and salario <= 1200):
	porcentagem = salario * (30/100)
	total = salario + porcentagem
elif (salario > 1200 and salario <= 1400):
	porcentagem = salario * (20/100)
	total = salario + porcentagem
elif (salario > 1400 and salario <= 1600):
	porcentagem = salario * (10/100)
	total = salario + porcentagem
else:
	porcentagem = salario * (5/100)
	total = salario + porcentagem
	
if(valido == False):
	print('Dado invalido')
else: 
	novo_salario = round(total, 2)
	print('Novo salario: R$ {}'.format(novo_salario))