numero = int(input())
cont = 0
while(numero != -1):
	if numero >= 26 and numero <= 50:
		cont += 1
	numero = int(input())		
print(cont)