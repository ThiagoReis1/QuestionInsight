x = int(input("Determine x: "))

if x % 47 == 0:
	print(int(x / 47))
	print("sim")
else:
	print(x % 47)
	print("nao")