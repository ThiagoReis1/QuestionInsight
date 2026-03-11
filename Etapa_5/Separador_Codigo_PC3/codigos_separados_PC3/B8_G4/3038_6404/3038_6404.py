from math import *

x = float(input(": "))

if x <= -1 or x >= 1:
	f_x = sqrt(abs(x))
elif -1 < x < 0 or 0 < x < 1:
	f_x = abs(x)
elif x == 0:
	f_x = 0
	
print(round(f_x, 2))