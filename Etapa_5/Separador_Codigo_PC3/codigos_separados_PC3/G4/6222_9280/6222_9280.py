x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))

soma = 0

i = x

while (i <= y):
	if i % 2 == 0 :
		soma += i
	i += 1
print(soma)