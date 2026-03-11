x = int(input("qual o valor de x: "))

if x % 31 == 0:
	d = x // 31
	print(d)
	print("sim")
else:
	d = x % 31
	print(d)
	print("nao")