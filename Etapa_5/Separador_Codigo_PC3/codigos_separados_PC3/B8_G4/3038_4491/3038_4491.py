from math import *

# entrada valor de x

x = float(input("valor de x: "))

if (x <= -1) or (x >= 1):
	form = abs(x) ** (1/2)
elif (x > -1 and x > 0) or (x < 0 and x < 1):
	form = abs(x)
elif (x == 0):
	form = 0
print(round(form, 2))