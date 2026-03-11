n = int(input("digite o numero: "))

if (n % 29 == 0):
	quo = n // 29
	print(quo)
	print("sim")
else:
	resto = n % 29
	print(resto)
	print("nao")
