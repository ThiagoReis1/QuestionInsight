n = int(input("numero: "))
cont = 0

while (n >= 0):
	if (n >= 26) and (n <= 85):
		cont = cont + 1
	n = int(input("numero: "))
print(cont)