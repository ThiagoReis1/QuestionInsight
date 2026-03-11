num = int(input("Quantidade de numeros: "))
acum = 0

while num >= 0:
	if num >= 76 and num <= 100:
		acum = acum + 1
	num = int(input("Quantidade de numeros: "))
print(acum)