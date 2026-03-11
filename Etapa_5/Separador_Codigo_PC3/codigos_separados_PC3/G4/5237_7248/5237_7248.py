x = int(input())
y = int(input())
z = int(input())

if (x and y % 2 == 0) and (y and z % 2 == 0) or (x and z % 2 == 0):
	print("SIM")
else:
	print("NAO")