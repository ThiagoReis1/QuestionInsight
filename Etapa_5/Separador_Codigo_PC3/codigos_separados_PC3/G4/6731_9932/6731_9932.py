x = int(input())

if x % 47 == 0:
	z = x//47
	print(z)
	print("sim")
else:
	z = x % 47
	print(z)
	print("nao")