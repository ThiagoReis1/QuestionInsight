x = int(input("Informe valor de x: "))
y = int(input("Informe valor de y: "))
n = x
soma = 0

while (n <= y):
	if (n % 3 == 0):
		soma += n
	
	n += 1
	
print(soma)
