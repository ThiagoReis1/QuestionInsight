a = int(input("Valor: "))

cont = 0

while a >= 0:
	if 45 <= a <= 150:
		cont = cont + 1
	else:
		cont = cont
	a = int(input("Valor: "))	

print(cont)