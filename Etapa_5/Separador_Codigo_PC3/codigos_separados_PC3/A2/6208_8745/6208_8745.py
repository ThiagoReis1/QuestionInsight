num_sorte = int(input("Digite o numero: "))
cont = 0

while (num_sorte != -1):
	num_sorte = int(input("Digite o numero: "))
	if (num_sorte >= 51 and num_sorte <= 75):
		cont = cont + 1
	else:
		cont = cont
print(cont)