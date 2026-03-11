x = float(input("preco de custo: "))

a = 2 * x
b = x + (50 / 100) * x
c = x + (40 / 100) * x
d = x + (30 / 100) * x

if(x < 50):
	print(round(a, 2))
elif((x > 50.01) and (x <= 100)):
	print(round(b, 2))
elif((x > 100.01) and (x <= 500)):
	print(round(c, 2))
elif(x > 500):
	print(round(d, 2))