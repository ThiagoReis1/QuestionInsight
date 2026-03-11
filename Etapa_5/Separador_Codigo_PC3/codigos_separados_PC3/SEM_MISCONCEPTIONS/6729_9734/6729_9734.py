x = int(input("x"))

if x% 41 == 0:
	resto = x // 41
	print(resto)
	print("sim")
else: 
	resto = x % 41
	print(resto)
	print("nao")