from math import*
x = float(input("valor de x: "))
if (x <= 1):
	cal = 1
elif (1 < x <= 2):
	cal = 2
elif (2 <  x <= 3):
		cal = x ** 2
else:
		cal = x ** 3

print(round(cal,2))
	

	
	