num = int(input("Numero verificador: "))
cont = 0
while num > -1:
	if 45 <= num and num <= 150:
		cont += 1
	num = int(input("Numero verificador: "))
print(cont)