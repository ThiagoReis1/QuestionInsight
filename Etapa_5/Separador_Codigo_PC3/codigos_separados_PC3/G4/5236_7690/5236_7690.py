n = int(input("N: "))
if (n % 3 == 0) and (n % 5 == 0):
	print("PirlimPimpim")
elif (n % 3 == 0):
	print("Pirlim")
elif (n % 5 == 0):
	print("Pimpim")
else:
	print(n)