x = int(input("Insira o valor de x: "))
y = int(input("Insira o valor de y: "))

i = x
soma = 0

while x <= y:
	if x % 2 != 0:
		soma += x
	x += 1

print(soma)