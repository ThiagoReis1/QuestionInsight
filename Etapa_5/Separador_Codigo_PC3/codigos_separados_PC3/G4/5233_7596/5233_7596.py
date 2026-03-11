n = int(input("numero inteiro: "))
r1 = n % 3
r2 = n % 5

if (n >= 1):
	if (r1 == 0) and (r2 == 0):
		print("AuauMiau")
	elif (r2 == 0):
		print("Miau")
	elif (r1 == 0):
		print("Auau")
	else:
		print(n)