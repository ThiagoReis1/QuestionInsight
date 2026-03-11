x=float(input("valor de x: "))

if x <= -1 or x >= 1:
	t = x**2
elif -1 < x < 0 or 0 < x < 1:
	t = x
elif x == 0:
	t = 1
	
print(round(t, 4))