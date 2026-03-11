from math import *
x = float(input(""))

if x <= 0:
	total = 0
elif (0 < x) and (x <= 1):
	total = 1
elif (1 < x) and (x <= 2):
	total = x**(1/2)
else:
	total = x**(1/3)
print(round(total,4))