n = int(input("numero: "))

if n >= 1:
	if n % 3 == 0 and n % 5 != 0:
		print("Plunct")
	elif n % 5 == 0 and n % 3 != 0:
		print("Plact")
	elif n % 3 == 0 and n % 5 == 0:
		print("Zuuum")
	else:
		print(n)