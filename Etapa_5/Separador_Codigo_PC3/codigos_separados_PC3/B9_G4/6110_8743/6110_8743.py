q = float(input("Digite um numero: "))

if (q < 17.5):
	x = 10.5 + q
	print(round(x,1))
elif (q >= 17.5 and q < 35.0):
	y = 14.0 + q
	print(round(y,1))
elif (q >= 35.0 and q < 50.0):
	z = 18.6 + q
	print(round(z,1))
else:
	t = 24.5 + q
	print(round(t,1))