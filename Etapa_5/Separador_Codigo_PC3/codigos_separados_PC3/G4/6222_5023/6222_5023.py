x = int(input("Valor de X: "))
y = int(input("Valor de Y: "))
c = x
soma = 0
while (c <= y):
	if (c % 2 == 0):
		soma = soma + c
	c = c + 1
print(soma)
	