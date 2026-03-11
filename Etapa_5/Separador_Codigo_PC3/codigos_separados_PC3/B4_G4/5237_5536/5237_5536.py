a = int(input("numeros inteiros: "))
b = int(input("numeros inteiros: "))
c = int(input("numeros inteiros: "))

if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
	print ("SIM")
elif (a % 2 == 0 and b % 2 == 0):
	print("SIM")
elif (b % 2 == 0 and c % 2 == 0):
	print("SIM")
elif (a % 2 == 0 and c % 2 == 0):
	print("SIM")	
	
else:
	print("NAO")
	