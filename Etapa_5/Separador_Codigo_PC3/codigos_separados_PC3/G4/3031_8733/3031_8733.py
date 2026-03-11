x = float(input("numero real x : "))

if x <= 1:
	print(round(1,2))
elif 1 < x <= 2:
	print(round(2,2))
elif 2 < x <= 3:
	print(round(x ** 2,2))
else:
	print(round(x ** 3,2))