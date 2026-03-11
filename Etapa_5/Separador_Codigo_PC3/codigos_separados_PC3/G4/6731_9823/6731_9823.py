x = int(input())

if x % 47 == 0:
	x1 = (x//47)
	print(x1)
	print("sim")
else:
	x1 = (x % 47)
	print(x1)
	print("nao")