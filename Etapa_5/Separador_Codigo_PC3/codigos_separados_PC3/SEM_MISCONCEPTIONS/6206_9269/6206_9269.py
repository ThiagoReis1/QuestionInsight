intervalo = int(input("digite o numero: "))
cont = 0

while (intervalo != -1):
	if (0 <= intervalo <= 25):
		cont = cont + 1
	intervalo = int(input("digite o numero: "))
print(cont)
