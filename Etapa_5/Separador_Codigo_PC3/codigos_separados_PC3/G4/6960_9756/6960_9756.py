x = int(input("Informe o valor de X: "))
y = int(input("Informe o valor de y: "))
cont = 0
i = x

while x<=y:
	if i % 2 != 0:
		cont = cont + 1
	x = x +1
print (cont)