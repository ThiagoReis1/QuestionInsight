#% é o resto

n = int(input("numero:"))

if n >= 1:
	if ( n % 3) == 0 and (n % 5) == 0:
		print("AuauMiau")
	elif ( n % 5) == 0:
		print("Miau")
	elif ( n % 3) == 0:
		print("Auau")
	else:
		print(n)

else: 
	print(n)
