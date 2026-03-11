x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))
soma = 0

for num in range(x, y + 1):
	if num % 2 == 0:
		soma += num
print(soma)
		