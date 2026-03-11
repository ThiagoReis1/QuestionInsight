a = int(input(""))
b = int(input(""))
c = int(input(""))

a1 = a % 2
b2 = b % 2
c2 = c % 2

if a1 == 0 and b2 == 0 and c2 == 0:
	print("SIM")
elif a1 == 0 and b2 == 0:
	print("SIM")
elif a1 == 0 and c2 == 0:
	print("SIM")
elif b2 == 0 and c2 == 0:
	print("SIM")
else:
	print("NAO")