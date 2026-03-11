n1 = int(input("Numero1:"))
n2 = int(input("Numero2:"))
n3 = int(input("Numero3:"))

if (n1 >= 1000 and n2 >= 1000):
	print("SIM")
elif (n2 >= 1000 and n3 >= 1000):
	print("SIM")
elif (n3 >= 1000 and n1 >= 1000):
	print("SIM")
else:
	print("NAO")