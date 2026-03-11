numero = int(input("digite o numero: "))
cont = 0

while(numero != -1):
	if(101 <= numero <= 201):
		cont = cont  + 1
	numero = int(input("digite o numero: "))
print(cont)