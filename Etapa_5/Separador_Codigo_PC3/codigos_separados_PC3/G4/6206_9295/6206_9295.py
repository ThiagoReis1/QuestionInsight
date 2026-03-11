num = int(input("Digite os numeros: "))
cont = 0

while (num != -1):
	if (0 <= num <= 25):
		cont = cont + 1
	num = int(input("Digite os numeros: "))
	
print(cont)