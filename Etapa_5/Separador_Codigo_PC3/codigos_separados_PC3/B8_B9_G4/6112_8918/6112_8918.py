q = float(input("Digite um numero: "))

if (q < 17.5):
	x = 10.5 + q
	print(round(x, 1))
elif (q >= 17.5 and q < 35.0):
	b = 14.0 + q
	print(round(b, 1))
elif (q >= 35.0 and q < 50.0):
	f = 18.6 + q
	print(round(f, 1))
elif (q >= 50.0):
	g = 24.5 + q
	print(round(g, 1))
	