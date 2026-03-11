num = int(input("Digite um numero negativo: "))
cont = num

if num % 3 == 0:
	print(num)

while cont != 0:
	cont += 1		
	if cont % 3 == 0:
		print(cont)
		

print("fim")