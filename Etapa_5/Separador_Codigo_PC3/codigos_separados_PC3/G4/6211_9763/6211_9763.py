n = int(input("Informe o numero escolhido: "))
cont = 0

while (n != -1):
	if (100 <= n <= 199):
		cont = cont + 1
	n = int(input("Informe o numero escolhido: "))
print(cont)