c = float(input("Quantidade de combustivel: "))

if (c < 17.5):
	total = c + 0.8
elif (c >= 17.5) and (c < 35.0):
	total = c + 1.3
elif (c >= 35.0) and (c < 50.0):
	total = c + 2.1
elif (c >= 50.0):
	total = c + 3.0
	
print(round(total, 1))