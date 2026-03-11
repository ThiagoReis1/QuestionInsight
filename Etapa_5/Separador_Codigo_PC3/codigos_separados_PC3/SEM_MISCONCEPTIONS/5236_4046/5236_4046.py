num_int = int(input("Informe um numero inteiro: "))

if(num_int >= 1):
	if(num_int % 3 == 0 and num_int % 5 == 0):
		print("PirlimPimpim")
	elif(num_int % 3 == 0):
		print("Pirlim")
	elif(num_int % 5 == 0):
		print("Pimpim")
	else:
		print(num_int)
else:
	print(num_int)