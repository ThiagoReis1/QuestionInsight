x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
cont = 0

while (x < y):
	if (x % 7 == 0) or (y % 7 == 0):
		cont = cont + 1
	print(cont)
