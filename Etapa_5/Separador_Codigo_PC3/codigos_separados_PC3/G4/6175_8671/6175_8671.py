x = float(input("x: "))

if (x >= -4) and (x < 0):
	f = abs(x) ** 0.5
	print(round(f, 4))
elif (x >= 0) and (x <= 4):
	f = x ** 0.5
	print(round(f, 4))
else:
	print("entrada invalida")