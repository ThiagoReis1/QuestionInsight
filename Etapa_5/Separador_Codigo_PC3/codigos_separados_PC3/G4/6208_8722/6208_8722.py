n = int(input("Digite um numero: "))
cont = 0

while (n > -1):
	if (n>=51) and (n<=75):
		cont = cont + 1
	n = int(input("Digite um numero: "))
	
print(cont)