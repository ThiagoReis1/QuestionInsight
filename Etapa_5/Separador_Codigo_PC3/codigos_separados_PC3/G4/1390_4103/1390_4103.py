a = float(input("Quantidade de minutos: "))
x = a * 1.20
y = (a * 1.40) + 25

if (a <= 100):
	print(round(x, 2))
else:
	print(round(y, 2))