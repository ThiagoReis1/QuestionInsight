n1 = int(input("N: "))
n2 = int(input("N: "))
n3 = int(input("N: "))

if((n1 >= 1000 and n2 >= 1000) or (n1>= 1000 and n3 >= 1000) or (n2 >= 1000 and n1 >= 1000) or (n2 >= 1000 and n3 >= 1000) or (n3 >= 1000 and n1 >=1000) or (n3 >= 1000 and n2 >= 1000)):
	print("SIM")
else:
	print("NAO")