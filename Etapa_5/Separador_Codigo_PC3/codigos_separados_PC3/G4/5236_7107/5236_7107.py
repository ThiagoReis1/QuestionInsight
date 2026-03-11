n = int(input())

if(n >= 1):
	if(n % 3 == 0 and n % 5 == 0):
		st = "PirlimPimpim"

	elif(n % 5 == 0):
		st = "Pimpim"

	elif(n % 3 == 0):
		st = "Pirlim"

	else:
		st = n

	print(st)
	
else:
	print(n)