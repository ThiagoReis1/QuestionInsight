num = int(input("insira o numero: "))


cont = 0

while num >= 0:
	if num >= 35 and num <= 95:
		cont += 1
	num = int(input("insira o numero: "))	
print(cont)