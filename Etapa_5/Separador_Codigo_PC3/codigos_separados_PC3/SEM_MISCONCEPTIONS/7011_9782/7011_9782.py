x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

contadora = x

while contadora <= y:
	if (contadora%5 == 0):
		print(contadora)
	contadora += 1
	
	