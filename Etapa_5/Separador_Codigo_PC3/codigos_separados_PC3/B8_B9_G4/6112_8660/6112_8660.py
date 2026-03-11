x = (float(input("quantidade de combustivel: ")))

if (x < 17.5):
	z = x + 10.5
elif (x >= 17.5)and(x < 35):
		z = x + 14
elif (x >= 35) and (x < 50):
		z = x + 18.6
elif (x >= 50):
		z = x + 24.5
print(round(z, 2))