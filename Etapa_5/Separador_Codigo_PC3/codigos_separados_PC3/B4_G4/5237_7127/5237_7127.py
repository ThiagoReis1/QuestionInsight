a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))

if (a % b == 0) and (a % c == 0) and (b % c == 0):
	print("SIM")
elif(a % b == 2):
	print("SIM")
elif(a % c == 2):
	print("SIM")
elif(b % c == 2):
	print("SIM")
else:
	print("NAO")