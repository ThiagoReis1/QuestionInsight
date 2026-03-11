x = float(input())
y = float(input())
z = float(input())

if(x >= 0 and y >= 0 and z >= 0):
	if((x % 2 and y % 2 or z % 2) == 0):
		print("SIM")
	else:
		print("NAO")