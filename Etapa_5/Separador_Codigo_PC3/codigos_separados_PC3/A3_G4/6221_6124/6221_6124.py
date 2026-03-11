x = int(input("Valor de x: "))
y = int(input("Valor de y: "))

while x // 7 and y // 7:
	if x < y:
		valor = x + y
		acum = acum + 1
		print(acum)