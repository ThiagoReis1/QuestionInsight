X = int(input("N: "))

if X % 41 == 0:
	R = X // 41
	print(R)
	print("sim")
else:
	T = X % 41
	print(T)
	print("nao")
	