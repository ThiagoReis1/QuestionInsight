x = float(input("numero:"))
if x <= -1 or x >= 1:
	cal = x**2
	print(round(cal,4))
elif -1 < x < 0 or 0 < x < 1:
	cal = x
	print(round(cal,4))
else:
	cal = 1
	print(round(cal,4))