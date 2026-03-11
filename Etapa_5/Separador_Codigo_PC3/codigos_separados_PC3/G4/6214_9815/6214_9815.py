n = int(input("Insira os Valores: "))
cont = 0

while n != -1:
	if n >= 45 and n <= 150:
		cont += 1
		n = int(input("Insira outro Valor: "))
	else:
		n = int(input("Insira outro Valor: "))
		
print(cont)