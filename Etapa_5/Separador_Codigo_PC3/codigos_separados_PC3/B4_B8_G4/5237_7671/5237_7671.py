#Numeros Pares

a = int(input("Digite o primeiro numero: "))

b = int(input("Digite o segundo numero: "))

c = int(input("Digite o terceiro numero: "))

if((a % 2 == 0) or(b % 2 == 0) or (c % 2 == 0)):
	if((a % 2 != 0) and (b % 2 == 0) and (c % 2 == 0)):
		print("SIM")
	elif((a % 2 == 0) and (b % 2 != 0) and (c % 2 == 0)):
		print("SIM")
	elif((a % 2 == 0) and (b % 2 == 0) and (c % 2 != 0)):
		print("SIM")
	elif((a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)):
		print("SIM")
	elif((a % 2 != 0) and(b % 2 != 0) and (c % 2 == 0)):
		print("NAO")
	elif((a % 2 != 0) and (b % 2 == 0) and (c % 2 != 0)):
		print("NAO")
	elif((a %2 == 0) and (b % 2 != 0) and (c % 2 != 0)):
		print("NAO")
else:
	print("NAO")
	