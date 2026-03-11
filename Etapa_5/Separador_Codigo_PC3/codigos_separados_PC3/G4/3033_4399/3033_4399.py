x = float(input())
if x >= -100 and x < 0:
	x = -(1/x)
	print(round(x, 4))
elif x > 0 and x <= 100:
	x = 1/x
	print(round(x, 4))
else:
	print("entrada invalida")