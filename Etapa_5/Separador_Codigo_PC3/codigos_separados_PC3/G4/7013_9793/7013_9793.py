x = int(input('x= '))
y = int(input('y = '))

cont = x
soma = 0

while cont <= y:
	if cont % 2 == 0:
		soma = soma + cont
	cont = cont + 1

print(soma)