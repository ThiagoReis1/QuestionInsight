x = int(input(""))
if (x % 31 == 0):
	q = x//31
	print(x // 31)
	print("sim")
else:
	r = x % 31
	print(x % 31)
	print("nao")
