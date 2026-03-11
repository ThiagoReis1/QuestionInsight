x = float(input("valor de x: "))

if(x <= 1):
	t = 1
	print(round(t, 2))
elif(1 < x <= 2):
	t = 2
	print(round(t, 2))
elif(2 < x <= 3):
	t = x**2
	print(round(t, 2))
elif(x > 3):
	t = x**3
	print(round(t, 2))