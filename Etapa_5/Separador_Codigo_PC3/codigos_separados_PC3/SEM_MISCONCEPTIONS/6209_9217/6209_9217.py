numero = int(input("Digite um numero: "))
cont = 0

while numero > 0:
	if numero >=76 and numero <= 100:
		cont = cont + 1
	numero = int(input("Digite um numero: "))
print(cont)