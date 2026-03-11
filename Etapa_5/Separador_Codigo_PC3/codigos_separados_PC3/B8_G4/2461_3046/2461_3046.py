p = float(input("informe o preco: "))

a = 2 * p
b = p + (50 / 100) * p
c = p + (40 / 100) * p
d = p + (30 / 100) * p

if(0 <= p <= 50):
	print(round(a, 2))
elif(50.01 <= p <= 100):
	print(round(b, 2))
elif(100.01 <= p <= 500):
	print(round(c, 2))
elif(p > 500):
	print(round(d, 2))