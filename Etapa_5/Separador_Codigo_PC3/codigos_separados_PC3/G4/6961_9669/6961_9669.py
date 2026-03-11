x = int(input("Entre com o valor de x: "))
y = int(input("Entre com o valor de y: "))

soma = 0
while x <= y:
	if x % 3 == 0:
		soma = soma + x
	x = x + 1

print(soma)
	