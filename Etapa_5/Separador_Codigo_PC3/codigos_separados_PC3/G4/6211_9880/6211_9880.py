num = int(input("Insira o numero desejado: "))

cont = 0
	
while num >= 0:
	if 100 <= num <= 199:
		cont += 1
	if num >= 0:
		num = int(input("Insira o numero desejado: "))

print(cont)