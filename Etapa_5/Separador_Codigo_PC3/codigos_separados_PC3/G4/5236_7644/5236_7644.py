n = int(input("Valor N: "))
if(n%3 == 0) and (n%5 == 0):
	print("PirlimPimpim")
elif (n%5 == 0):
	print("Pimpim")
elif (n%3 == 0):
	print("Pirlim")
else:
	print(n)