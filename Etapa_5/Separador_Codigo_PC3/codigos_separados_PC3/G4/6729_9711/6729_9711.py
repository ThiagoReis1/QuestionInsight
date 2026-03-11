x = int(input("qual o valor de x?"))
div = x // 41
rest = x % 41
if x % 41 == 0:
	print(div)
	print("sim")
else:
	print(rest)
	print("nao")