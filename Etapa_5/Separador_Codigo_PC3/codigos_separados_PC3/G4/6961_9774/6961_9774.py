nx = int(input("N. X: "))
ny = int(input("N. Y: "))

soma = 0

while (nx <= ny):
	if (nx % 3 == 0):
		soma += nx
	nx += 1
		
print(soma)