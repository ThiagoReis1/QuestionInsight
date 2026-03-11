x = float(input("Digite X: "))

if -1000 <= x and x <= -2:
	c = -(1) / (x +2)
	print(round(c,4))

elif 2 <= x and x <= 1000:
	c = 1 / (x - 2)
	print(round(c,4))
else:
	print("entrada invalida")