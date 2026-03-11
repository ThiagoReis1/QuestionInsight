x = int(input("insira um numero inteiro"))
if x % 43 ==0:
	q = x // 43
	print(q)
	print("sim")
else:
	resto = x % 43
	print(resto)
	print("nao")
	