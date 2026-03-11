x = int(input("qual valor de X? "))
div = x // 43
rest = x % 43
if x % 43 == 0:
	print(div)
	print("sim")
else:
	print(rest)
	print("nao")