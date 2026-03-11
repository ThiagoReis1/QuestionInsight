X = int(input("X? "))
if X%31 == 0:
	print(X//31)
	print("sim")
else:
	print(X%31)
	print("nao")