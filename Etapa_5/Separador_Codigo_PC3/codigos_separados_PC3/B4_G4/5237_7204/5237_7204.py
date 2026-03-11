x = int(input("inteiro 1: "))
y = int(input("inteiro 2: "))
z = int(input("inteiro 3: "))

if x%2 == 0 and y%2 == 0 and z%2 == 0:
	print("SIM")
elif (x%2 == 0 and y%2 == 0) or (y%2 == 0 and z%2 == 0) or (x%2 == 0 and z%2 == 0):
	print("SIM")
else:
	print("NAO")