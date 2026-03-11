num = int(input("Digite um valor: "))
cont = 0

while num != -1:
	if num >= 45 and num <= 150:
		cont += 1
	num = int(input("Digite um valor: "))	
		
print(cont)