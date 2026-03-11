x = int(input("X: "))

d = x%13

if d == 0:
	print(x//13)
	print("sim")
else:
	print(d)
	print("nao")

