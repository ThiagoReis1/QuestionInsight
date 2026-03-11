a = float(input("Quantidade de combustivel comum: "))
c = a + 10.5
d = a + 14.0
e = a + 18.6
f = a + 24.5
if (0 < a < 17.5):
	print(round(c, 2))
elif (a >= 17.5) and (a < 35):
	print(round(d, 2))
elif (a >= 35) and (a < 50):
	print(round(e, 2))
else: 
	(a > 50)
	print(round(f, 2))