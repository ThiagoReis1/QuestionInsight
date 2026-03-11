num = int(input("Digite o numero: "))

if (num % 3 == 0)and (num % 5 == 0):
	print("PirlimPimpim")
elif (num % 5 == 0):
	print("Pimpim")
elif (num % 3 == 0):
	print("Pirlim")
else:
	print(num)