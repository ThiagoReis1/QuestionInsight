x = int(input("Valor de x: "))
y = int(input("Valor de y: "))

cont = x
soma = cont

while x < y:
	cont = cont + 1
	
	if cont / 2 == 0:
		soma = soma + cont
		print(soma)