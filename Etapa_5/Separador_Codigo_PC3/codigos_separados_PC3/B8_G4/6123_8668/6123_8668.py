c = int(input("quantidade de combustivel: "))

if (c > 0) and (c < 17.5):
	l = c + 0.8
	print(round(l, 1))
elif (c > 0) and (c >= 17.5) and (c < 35):
	l = c + 1.3
	print(round(l, 1))
elif (c > 0) and (c >= 35) and (c < 50):
	l = c + 2.1
	print(round(l, 1))
elif (c >= 50):
	l = c + 3
	print(round(l, 1))