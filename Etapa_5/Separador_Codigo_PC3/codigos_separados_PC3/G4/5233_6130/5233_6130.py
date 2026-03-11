n = int(input("digite um numero: "))

if (n % 3) == 0:
	print("Auau")
elif (n % 5) == 0:
	print("Miau")
elif (n % 3) == 0 and (n % 5) == 0:
	print("AuauMiau")
else:
	print(n)