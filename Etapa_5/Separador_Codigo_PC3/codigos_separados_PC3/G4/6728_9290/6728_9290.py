num = int(input("numero: "))
##################
if num % 37 == 0:
	x = num // 37
	print(x)
	print("sim")
else:
	x = num % 37
	print(x)
	print("nao")