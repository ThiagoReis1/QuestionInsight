x = int(input("x: "))

if x % 17 == 0:
	qd = x // 17
	print(qd)
	print("sim")
	
else:
	resto = x % 17
	print(resto)
	print("nao")