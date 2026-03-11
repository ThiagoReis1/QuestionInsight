x = float(input("digite o num: "))

if x <= -4 or x < 0:
	f = abs(x**0.5)
	print(round(f, 4))
elif x <= 0 or x <= 4:
	f = x**0.5
	print(round(f, 4))
elif x > 4:
	print("entrada invalida")

