x = int (input("Digite o valor de x: "))
y = int (input("Digite o valor de y: "))
soma = 0
while (x <= y):
	resto = x % 7
	if (resto == 0):
		soma = soma + x
	x = x + 1
print (soma)