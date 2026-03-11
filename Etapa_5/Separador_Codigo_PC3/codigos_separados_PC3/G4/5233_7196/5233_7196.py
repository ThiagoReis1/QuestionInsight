n = int(input(""))

if (n >= 1):
	if (n % 3 == 0) and (n % 5 == 0):
		print("AuauMiau")
	elif(n % 3 == 0):
		print("Auau")
	elif (n % 5 == 0):
		print("Miau")
	else:
		print(n)
else:
	print(n)