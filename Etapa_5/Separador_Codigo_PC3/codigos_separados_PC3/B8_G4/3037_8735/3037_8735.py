x = float(input("digite o valor de x: "))

if x <= -1 or x >= 1:
	print(round(x**2, 4))

elif -1 < x < 0 or 0 < x < 1:
	print(x)

elif x == 0:
	print(1)