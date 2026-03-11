x = int(input("x:"))

if x % 41 == 0:
	q = x // 41
	print(q)
	print("sim")
else:
	resto = x % 41
	print(resto)
	print("nao")
	
