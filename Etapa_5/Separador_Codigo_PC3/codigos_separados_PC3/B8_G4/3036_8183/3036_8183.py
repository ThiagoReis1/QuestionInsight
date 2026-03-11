X = float(input("Valor de X: "))

if (X <= -1 or X >= 1):
	print(round(X, 2))
	
elif ((X > -1 and X < 0) or (X > 0 and X < 1)):
	print("1")
	
elif (X == 0):
	print("2")