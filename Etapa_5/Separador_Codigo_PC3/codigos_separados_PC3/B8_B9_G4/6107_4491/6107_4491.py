# entrada eh a quantidade de combustivel comum 

q = float(input("quantidade de combustivel: "))
x = 17.5
y = 35.0
z = 50.0

if (q > 0):
	if (q < x):
		form = q + 1.5
	elif (q >= x and q <= y):
		form = q + 2.3
	elif (q >= y and q <= z):
		form = q + 3.3
	elif (q >= z):
		form = q + 4.7
print(round(form, 1))