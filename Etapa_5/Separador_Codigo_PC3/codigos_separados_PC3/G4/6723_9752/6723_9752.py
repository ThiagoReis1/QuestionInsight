num = int(input())

if (num % 19) == 0:
	A = num // 19
	print(A)
	print("sim")
else:
	Y = num % 19
	print(Y)
	print("nao")