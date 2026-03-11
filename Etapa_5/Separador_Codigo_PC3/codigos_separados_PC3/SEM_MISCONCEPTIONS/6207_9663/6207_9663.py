n = int(input("Digite o valor de n para a variavel: "))

contadora = 0

while (n != -1):
	if (26 < n and n < 50):
		contadora = contadora + 1
	n = int(input("Digite o valor de n para a variavel: "))

print(contadora)