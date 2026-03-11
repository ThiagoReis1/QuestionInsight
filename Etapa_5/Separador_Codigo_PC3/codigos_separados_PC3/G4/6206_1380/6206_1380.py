n = int(input("Informe valor de n: "))
cont = 0

while (n != -1):
	
	if (n >= 0 and n <= 25):
		cont += 1
	
	n = int(input("Informe valor de n: "))
	
print(cont)
