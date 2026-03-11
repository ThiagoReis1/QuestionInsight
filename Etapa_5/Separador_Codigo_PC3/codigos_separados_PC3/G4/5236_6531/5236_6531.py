n = int(input("valor de N: "))

if( n % 3 == 0 and not n % 5 == 0):
	print("Pirlim")
elif(n % 5 == 0 and not n % 3 == 0):
	print("Pimpim")
elif(n % 3 == 0 and n % 5 == 0):
	print("PirlimPimpim")
else:
	print(n)
 
