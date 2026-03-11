x = int(input("Valor de X: "))
y = int(input("Valor de Y: "))

cont = 0

while (x <= y):
	if (x % 7 ==  0):
		cont = cont + x
	x = x + 1
print(cont)
	
	