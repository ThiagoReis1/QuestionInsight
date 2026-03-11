x = int(input("valor de x: "))
y = int(input("valor de y: "))

soma = 0

while x <= y:
	if x % 7 == 0:
		soma = soma + x
	x = x + 1
	
print(soma)
