num = int(input("Digite um numero: "))

cont = 0
cont2 = 0

while (num != 0):
	cont = cont + 1
	
	if (num > 0):
		cont2 = cont2 + 1
	num = int (input("Digite um numero: "))
x = (cont2 *100) / cont
	
print(cont)
print(round(x, 2))
