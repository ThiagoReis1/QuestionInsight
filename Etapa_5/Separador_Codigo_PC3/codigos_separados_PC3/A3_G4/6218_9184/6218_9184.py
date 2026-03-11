x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

soma = 0
resto = x % 2

if resto == 1:
	x += 1

while x <= y:
	print(x)
	x += 2