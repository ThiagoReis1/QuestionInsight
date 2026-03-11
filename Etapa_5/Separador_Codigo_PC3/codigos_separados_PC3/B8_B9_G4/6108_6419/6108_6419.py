a = float(input("quantidade de combustivel: "))

if a < 17.5:
	b = a +  1.5
	print(round(b, 1))
elif (a >= 17.5) and (a <= 35):
	c = a + 2.3
	print(round(c, 1))
elif (a >= 35) and (a == 50):
	d = a + 3.3
	print(round(d, 1))
elif (a > 50.0):
	c = a + 4.7
	print(round(c, 1))